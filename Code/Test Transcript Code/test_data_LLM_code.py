from ollama import chat
import os
from prompts_final import Prompts
import tiktoken
import sys

# output and transcript folders
TRANSCRIPT_DIR = "final_transcripts"
OUTPUT_DIR = "final_outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# get the prompts from the prompts.py file
prompts = {
    "zero_shot": Prompts.getZeroShot(),
    "few_shot": Prompts.getFewShot(),
    "cot": Prompts.getCOT()
}

# load the transcript
def load_transcript(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

# save the response to file
def save_response(output_path, prompt_name, prompt, response):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"PROMPT TYPE: {prompt_name}\n")
        f.write("=" * 50 + "\n")
        f.write(f"RESPONSE:\n{response}\n")

# estimate token usage to make sure we do not go over window
def estimate_tokens(text):
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))

# run the model inference
def run_with_streaming(full_prompt, model):
    response_text = ""
    # make inference call with set parameters
    stream = chat(
        model=model,
        messages=[{'role': 'user', 'content': full_prompt}],
        stream=True,
        options={
            'num_thread': os.cpu_count(),
            'num_ctx': 8192,
            'seed' : 42,
            'temperature' : 0.0,
            'top_p' : 1.0,
            'top_k' : 1
        }
    )
    # so we can see the output
    for chunk in stream:
        token = chunk['message']['content']
        response_text += token
        sys.stdout.write(token)
        sys.stdout.flush()
    print()
    return response_text

# define model types we are using
model_types = ["mistral:7b", "qwen2.5:7b", "gemma2:9b"]
 
# running the final evaluation

# for every transcripts in the test set
for filename in os.listdir(TRANSCRIPT_DIR):

    if filename.endswith(".txt"):

        transcript_name = filename.replace(".txt", "")
        transcript = load_transcript(os.path.join(TRANSCRIPT_DIR, filename))

        # for every prompt type
        for prompt_name, prompt in prompts.items():

            # for every model type
            for model in model_types:

                print(f"\n{'='*50}")
                print(f"Running: {transcript_name} | {prompt_name} | {model}")
                print('='*50)

                full_prompt = prompt + "\n\n" + transcript

                # estimate the tokens in the prompt
                tokens = estimate_tokens(full_prompt)

                MAX_CTX = 8192
                RESERVE = 1000 # spare tokens so we make sure we do not go overboard

                if tokens > (MAX_CTX - RESERVE):
                    print(f"Prompt is too long {tokens} tokens, skipping.")
                    continue
                else:
                    print("NOT TOO LARGE")

                answer = run_with_streaming(full_prompt, model)

                # get the outputs
                output_filename = f"{transcript_name}_{prompt_name}_{model.replace(':', '')}.txt"
                output_path = os.path.join(OUTPUT_DIR, output_filename)

                # save to folder
                save_response(output_path, prompt_name, full_prompt, answer)

                print(f"SAVED {output_filename}")
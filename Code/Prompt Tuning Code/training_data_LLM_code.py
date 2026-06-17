from ollama import chat
import os
from prompts_iter_1 import Prompts

TRANSCRIPT_DIR = "final_transcripts"
OUTPUT_DIR = "final_outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)

prompts = {
    "zero_shot": Prompts.getZeroShot(),
    "few_shot": Prompts.getFewShot(),
    "cot": Prompts.getCOT()
}

def load_transcript(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def save_response(output_path, prompt_name, prompt, response):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"PROMPT TYPE: {prompt_name}\n")
        f.write("=" * 50 + "\n")
        f.write(f"PROMPT:\n{prompt}\n")
        f.write("=" * 50 + "\n")
        f.write(f"RESPONSE:\n{response}\n")

for filename in os.listdir(TRANSCRIPT_DIR):
    if filename.endswith('.txt'):
        transcript_name = filename.replace('.txt', '')
        transcript = load_transcript(os.path.join(TRANSCRIPT_DIR, filename))

        for prompt_name, prompt in prompts.items():
            full_prompt = prompt + "\n\n" + transcript

            response = chat(
                model='llama3.1:8b',
                messages=[{'role': 'user', 'content': full_prompt}]
            )

            answer = response['message']['content']
            output_filename = f"{transcript_name}_{prompt_name}.txt"
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            save_response(output_path, prompt_name, full_prompt, answer)
            print(f"Saved: {output_filename}")
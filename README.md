# Ananya Singh Research Project

The data in this repository is a part of the CSE3000 Research Project 2026 as part of the Computer Science and Engineering Bachelor Degree. This research paper aims to answer the following : Can LLMs identify value, value tensions, and consensus points from multi-stakeholder deliberation transcripts?

## Structure

```text
+-- Annotation Data
|   +-- Final Test Annotations - Triangulated.xlsx
|   +-- Final Train Annotations - Triangulated.xlsx
|   +-- Test Set Annotations - Coder 1.xlsx
|   +-- Test Set Annotations - Coder 2.xlsx
|   +-- Training Set Annotations - Coder 1.xlsx
|   +-- Training Set Annotations - Coder 2.xlsx
|   +-- Metric Calculations.xlsx
|
+-- Code
|   +-- Prompt Tuning Code
|   |   +-- prompts_iter_1.py
|   |   +-- prompts_iter_2.py
|   |   +-- prompts_iter_3.py
|   |   +-- training_data_LLM_code.py
|   |
|   +-- Test Transcript Code
|   |   +-- prompts_final.py
|   |   +-- test_data_LLM_code.py
|   +-- LLM_as_a_judge_analysis_code.ipynb
|   +-- LLM_as_a_judge_code.ipynb
|
+-- LLM Outputs
|   +-- Cleanest_Test_Outputs
|   +-- Prompt_Tuning_Iteration_1
|   +-- Prompt_Tuning_Iteration_2
|   +-- Prompt_Tuning_Iteration_3
|   +-- Test_Transcripts_Outputs
|   +-- LLM_as_a_judge_scores.json
|
+-- Transcripts
|   +-- Training Transcripts
|   +-- Test Transcripts
```

- Annotation Data: This contains all the annotations/coding between the two annotators for both the training and test set as well as the triangulated results used for the final metric evaluation.
  - Metric Calculation : contains all false positive, false negative, true positive metrics for test and train transcripts as well as all metric calculations.

- Code : This contains all the Python scripts and notebooks used for the obtaining the LLM outputs and the LLM-as-a-judge-study.
  - Prompt Tuning Code : contains the Python files for all three iterations of the prompt tuning phase as well as the script to run the prompts with the LLM model.
  - Test Transcript Code : contains the final prompt file as well as the code the run the prompt with the three different LLM model.

- LLM Outputs: contains all from the outputs of the LLMs including the outputs of the training phase, testing phase and LLM-as-a-judge.
  - Note : Both the cleaned test outputs (where the file titles were anonymised as well as the content to prevent LLM information leaks) and normal outputs were provided, although most content between them are the same.

- Transcripts : contains all the training and test transcripts used in the study.
  - Training Transcripts : Contains the shortened five House of Commons transcripts that were used.
  - Test Transcripts : Contains the six artificially generated transcripts used.

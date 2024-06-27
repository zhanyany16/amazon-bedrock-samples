# Anthropic Claude-3 Haiku Fine-Tuning with Amazon Bedrock

This repository contains two Jupyter Notebooks that demonstrate how to fine-tune the Anthropic Claude-3 Haiku model using Amazon Bedrock.

## Notebooks

### 1. `00_Setup&DataPrep_Haiku.ipynb`

This notebook guides you through the process of setting up the necessary resources and preparing the datasets for fine-tuning the Anthropic Claude-3 Haiku model. It covers the following steps:

- Creating an IAM role and policies required for the fine-tuning process
- Preparing the CNN News Article dataset for training, validation, and testing
- Transforming the dataset into the required format for Haiku fine-tuning
- Creating an S3 bucket and uploading the processed datasets

### 2. `01_FinetuneClaudeHaikuModel.ipynb`

This notebook demonstrates the end-to-end process of fine-tuning the Anthropic Claude-3 Haiku model using Amazon Bedrock. It includes the following steps:

- Selecting the base model for fine-tuning
- Configuring hyperparameters for the fine-tuning job
- Creating and monitoring the fine-tuning job
- Creating provisioned throughput for the fine-tuned model
- Invoking the fine-tuned model and evaluating its performance
- Comparing the fine-tuned model's performance with the base model

## Prerequisites

- An AWS account with the necessary permissions to create and manage resources (IAM roles, S3 buckets, and Amazon Bedrock resources)
- Basic knowledge of Python and Jupyter Notebooks

## Usage

1. Clone this repository to your local machine or AWS Cloud9 environment.
2. Open the Jupyter Notebooks in the order specified (`00_Setup&DataPrep_Haiku.ipynb` followed by `01_FinetuneClaudeHaikuModel.ipynb`).
3. Follow the instructions provided in each notebook and execute the code cells sequentially.
4. Ensure that you are using the same kernel and instance across both notebooks for consistency.
5. Note that the fine-tuning process may take several hours to complete, depending on the dataset size and configured hyperparameters.

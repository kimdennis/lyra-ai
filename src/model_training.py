import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from datasets import load_dataset
import os

def train_model(dataset_path, output_dir, save_dir):
    # Select device: GPU if available, otherwise CPU
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    
    # Set pad_token as eos_token to avoid padding issues
    tokenizer.pad_token = tokenizer.eos_token

    # Load the model and move it to the selected device
    model = GPT2LMHeadModel.from_pretrained("gpt2").to(device)

    # Load the processed dataset
    dataset = load_dataset('csv', data_files=dataset_path)

    def tokenize_function(examples):
        tokenized_inputs = tokenizer(examples["lyrics"], padding="max_length", truncation=True, max_length=128)
        tokenized_inputs["labels"] = tokenized_inputs["input_ids"].copy()
        return tokenized_inputs

    tokenized_datasets = dataset.map(tokenize_function, batched=True)

    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=3,
        per_device_train_batch_size=4,  # Adjust this based on your GPU's capacity
        save_steps=10_000,
        save_total_limit=2,
        fp16=True if torch.cuda.is_available() else False,  # Enable mixed precision if on GPU
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
    )

    trainer.train()

    # Save the model and tokenizer
    model.save_pretrained(save_dir)
    tokenizer.save_pretrained(save_dir)

if __name__ == "__main__":
    # Get the absolute path of the current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define paths relative to the script directory
    dataset_path = os.path.join(script_dir, "../data/processed/filtered_lyrics.csv")
    output_dir = os.path.join(script_dir, "../models/checkpoints/")
    save_dir = os.path.join(script_dir, "../models/fine_tuned_model/")
    
    # Train and save the model
    train_model(dataset_path, output_dir, save_dir)

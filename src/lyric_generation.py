from transformers import GPT2Tokenizer, GPT2LMHeadModel
import os

def generate_lyrics(prompt, model_dir, max_length=150):
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained(model_dir)

    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2, top_p=0.95, temperature=0.7)

    generated_lyrics = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_lyrics

if __name__ == "__main__":
    # Get the absolute path of the current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define paths relative to the script directory
    model_dir = os.path.join(script_dir, "../models/fine_tuned_model/")
    output_file = os.path.join(script_dir, "../generated_lyrics/lyrics.txt")

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True)

    # Generate lyrics
    print("Generating lyrics...")
    lyrics = generate_lyrics("I'm beginning to feel like a Rap God", model_dir)
    print("Lyrics generated successfully.")

    # Save the generated lyrics to a file
    print(f"Saving lyrics to {output_file}...")
    with open(output_file, "w") as file:
        file.write(lyrics)
    print(f"Lyrics saved to {output_file}.")

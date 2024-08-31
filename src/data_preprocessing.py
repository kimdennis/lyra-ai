from datasets import load_dataset
import pandas as pd
import os

def load_and_filter_data(artist_name):
    dataset = load_dataset("sebastiandizon/genius-song-lyrics")
    filtered_dataset = dataset.filter(lambda example: artist_name.lower() in example['artist'].lower())
    return filtered_dataset

def save_filtered_data(filtered_dataset, output_path):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    df = pd.DataFrame(filtered_dataset['train'])
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    artist_name = "Eminem"  # Modify as needed

    # Get the absolute path of the current script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the output path relative to the script directory
    output_path = os.path.join(script_dir, "../data/processed/filtered_lyrics.csv")
    
    # Load and filter the data
    filtered_dataset = load_and_filter_data(artist_name)
    
    # Save the filtered data
    save_filtered_data(filtered_dataset, output_path)

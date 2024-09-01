# LyraAI - Lyric Script Generator

This project uses GPT-2 to generate lyrics based on a prompt. The script loads a fine-tuned GPT-2 model and generates text that resembles song lyrics.

## Project Structure

- `lyric_generation.py`: The main script for generating lyrics.
- `models/`: Directory containing the fine-tuned GPT-2 model.
- `generated_lyrics/`: Directory where the generated lyrics are saved.

## Dataset

This project uses the **Genius Song Lyrics** dataset, which is available on Hugging Face.

- **Dataset Name:** [Genius Song Lyrics](https://huggingface.co/datasets/sebastiandizon/genius-song-lyrics)
- **Source:** [Hugging Face Datasets](https://huggingface.co/datasets/sebastiandizon/genius-song-lyrics)
- **Description:** This dataset contains a large collection of song lyrics from various artists, sourced from the Genius website. It includes metadata such as the artist's name, song title, album, and the lyrics themselves.

This dataset is filtered based on the artist's name to fine-tune a GPT-2 model for generating lyrics in the style of a specific artist.

## Prerequisites

- Python 3.7 or later
- Virtual environment (optional but recommended)

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/lyra-ai.git
   cd lyra-ai

2. **Set up a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **3. Install Project Dependencies**

   ```bash
   pip install -r requirements.txt

4. **Preprocess the Data**

   ```bash
   python src/data_preprocessing.py

5. **Train the Model**
   
   ```bash
   python src/model_training.py

6. **Generate Lyrics**

   ```bash
   python src/lyric_generation.py

7. **Run Tests (Optional)**

   ```bash
   python -m unittest discover tests

# Lyric Generation Script

This project uses GPT-2 to generate lyrics based on a prompt. The script loads a fine-tuned GPT-2 model and generates text that resembles song lyrics.

## Project Structure

- `lyric_generation.py`: The main script for generating lyrics.
- `models/`: Directory containing the fine-tuned GPT-2 model.
- `generated_lyrics/`: Directory where the generated lyrics are saved.

### Prerequisites

- Python 3.7 or later
- Virtual environment (optional but recommended)

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/lyra-ai.git
   cd lyra-ai

2. **Set up a virtual environment:**

   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **3. Install Project Dependencies**

   pip install -r requirements.txt

4. **Preprocess the Data**

   python src/data_preprocessing.py

5. **Train the Model**
   
   python src/model_training.py

6. **Generate Lyrics**

   python src/lyric_generation.py

7. **Run Tests (Optional)**

   python -m unittest discover tests

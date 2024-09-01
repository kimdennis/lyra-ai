import unittest
import os
from src.lyric_generation import generate_lyrics

class TestLyricGeneration(unittest.TestCase):

    def test_generate_lyrics(self):
        prompt = "I'm beginning to feel like a Rap God"

        # Get the absolute path of the current script directory
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Define the model directory relative to the script directory
        model_dir = os.path.join(script_dir, "../models/fine_tuned_model/")
        
        # Generate lyrics
        lyrics = generate_lyrics(prompt, model_dir)

        # Ensure lyrics are generated
        self.assertTrue(len(lyrics) > 0)

if __name__ == "__main__":
    unittest.main()

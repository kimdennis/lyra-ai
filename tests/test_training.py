import os
import unittest
from src.model_training import train_model

class TestModelTraining(unittest.TestCase):

    def test_train_model(self):
        # Get the absolute path of the current test file directory
        test_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Define the dataset path relative to the test directory
        dataset_path = os.path.join(test_dir, "../data/processed/filtered_lyrics.csv")
        output_dir = os.path.join(test_dir, "../models/checkpoints/")
        save_dir = os.path.join(test_dir, "../models/fine_tuned_model/")
        
        # Print the dataset path for debugging
        print(f"Dataset path being used: {dataset_path}")
        
        # Ensure the dataset path is correct
        if not os.path.exists(dataset_path):
            self.fail(f"Dataset file not found: {dataset_path}")

        train_model(dataset_path, output_dir, save_dir)

if __name__ == "__main__":
    unittest.main()

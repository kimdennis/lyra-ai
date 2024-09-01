import unittest
from src.data_preprocessing import load_and_filter_data

class TestDataPreprocessing(unittest.TestCase):

    def test_load_and_filter_data(self):
        artist_name = "Eminem"
        dataset = load_and_filter_data(artist_name)
        self.assertGreater(len(dataset['train']), 0)

if __name__ == "__main__":
    unittest.main()

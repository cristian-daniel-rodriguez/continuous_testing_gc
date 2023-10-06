import unittest
import pandas as pd
from data_manipulation import DataManipulation
from loguru import logger

class TestDataManipulation(unittest.TestCase):
    """
    A class for testing the DataManipulation class.
    """

    def setUp(self):
        """
        Initializes a DataManipulation object with a test CSV file.
        """
        self.file_name = "test_data.csv"
        self.dm = DataManipulation(self.file_name)

    def test_file_exists(self):
        """
        Tests the file_exists method by checking if it correctly identifies the existence of a file.
        """
        # Test if file exists
        self.assertTrue(self.dm.file_exists())
        logger.info("File exists test passed")

        # Test if file does not exist
        self.dm.file_name = "non_existent_file.csv"
        self.assertFalse(self.dm.file_exists())
        logger.info("File does not exist test passed")

    def test_read_csv(self):
        """
        Tests the read_csv method by checking if it correctly reads a CSV file and returns a pandas DataFrame.
        """
        # Test if CSV file is read correctly
        expected_df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        self.assertEqual(self.dm.read_csv().to_dict(), expected_df.to_dict())
        logger.info("Read CSV test passed")

        # Test if function returns None when file does not exist
        self.dm.file_name = "non_existent_file.csv"
        self.assertIsNone(self.dm.read_csv())
        logger.info("Read CSV with non-existent file test passed")

    def test_drop_nan(self):
        """
        Tests the drop_nan method by checking if it correctly drops rows with NaN values from a pandas DataFrame.
        """
        # Test if NaN values are dropped correctly
        df = pd.DataFrame({"A": [1, 2, None], "B": [4, None, 6]})
        expected_df = pd.DataFrame({"A": [1], "B": [4]})
        self.assertEqual(self.dm.drop_nan(df).to_dict(), expected_df.to_dict())
        logger.info("Drop NaN test passed")

    def test_drop_duplicates(self):
        """
        Tests the drop_duplicates method by checking if it correctly drops duplicate rows from a pandas DataFrame.
        """
        # Test if duplicate rows are dropped correctly
        df = pd.DataFrame({"A": [1, 2, 2], "B": [4, 5, 5]})
        expected_df = pd.DataFrame({"A": [1, 2], "B": [4, 5]})
        self.assertEqual(self.dm.drop_duplicates(df).to_dict(), expected_df.to_dict())
        logger.info("Drop duplicates test passed")

if __name__ == '__main__':
    unittest.main()
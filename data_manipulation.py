import pandas as pd
from loguru import logger

# Class for data manipulation
class DataManipulation:
    # Function for initializing the class
    def __init__(self, file_name: str) -> None:
        """
        Initializes the DataManipulation class with the specified file name.

        Args:
            file_name (str): The name of the file to be manipulated.
        """
        self.file_name = file_name

    # Function for checking if a file exists, return error if not
    def file_exists(self) -> bool:
        """
        Checks if the specified file exists.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        try:
            open(self.file_name)
        except FileNotFoundError:
            logger.error("File not found")
            return False
        logger.info("File found")
        return True

    # Function for reading csv file, but before needs to check if the file exists
    def read_csv(self) -> pd.DataFrame:
        """
        Reads a CSV file with the specified file name.

        Returns:
            pandas.DataFrame: A pandas DataFrame containing the data from the CSV file.
        """
        if self.file_exists():
            logger.info("Reading CSV file")
            return pd.read_csv(self.file_name)
        
    # Function for dropping NaN values in pandas df
    def drop_nan(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Drops rows with NaN values from a pandas DataFrame.

        Args:
            df (pandas.DataFrame): The DataFrame to be manipulated.

        Returns:
            pandas.DataFrame: A pandas DataFrame with rows containing NaN values removed.
        """
        logger.info("Dropping NaN values")
        return df.dropna()
    
    # Function for dropping duplicates in pandas df
    def drop_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Drops duplicate rows from a pandas DataFrame.

        Args:
            df (pandas.DataFrame): The DataFrame to be manipulated.

        Returns:
            pandas.DataFrame: A pandas DataFrame with duplicate rows removed.
        """
        logger.info("Dropping duplicates")
        return df.drop_duplicates()
    
    # Function for dropping columns in pandas df
    def drop_columns(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        """
        Drops columns from a pandas DataFrame.

        Args:
            df (pandas.DataFrame): The DataFrame to be manipulated.
            columns (list): A list of column names to be dropped.

        Returns:
            pandas.DataFrame: A pandas DataFrame with the specified columns removed.
        """
        logger.info("Dropping columns")
        return df.drop(columns, axis=1)
    
    # Function for renaming columns in pandas df
    def rename_columns(self, df: pd.DataFrame, columns: dict) -> pd.DataFrame:
        """
        Renames columns in a pandas DataFrame.

        Args:
            df (pandas.DataFrame): The DataFrame to be manipulated.
            columns (dict): A dictionary of column names to be renamed, with the keys being the old names and the values being the new names.

        Returns:
            pandas.DataFrame: A pandas DataFrame with the specified columns renamed.
        """
        logger.info("Renaming columns")
        return df.rename(columns=columns)
    
    # Function for changing column type in pandas df
    def change_column_type(self, df: pd.DataFrame, column: str, type: str) -> pd.DataFrame:
        """
        Changes the data type of a column in a pandas DataFrame.

        Args:
            df (pandas.DataFrame): The DataFrame to be manipulated.
            column (str): The name of the column to be changed.
            type (str): The new data type of the column.

        Returns:
            pandas.DataFrame: A pandas DataFrame with the specified column's data type changed.
        """
        logger.info("Changing column type")
        return df[column].astype(type)
    
    # Function for saving pandas df to csv file
    def save_csv(self, df: pd.DataFrame, file_name: str) -> None:
        """
        Saves a pandas DataFrame to a CSV file.

        Args:
            df (pandas.DataFrame): The DataFrame to be saved.
            file_name (str): The name of the file to save the DataFrame to.

        Returns:
            None
        """
        logger.info("Saving CSV file")
        df.to_csv(file_name, index=False)
    

    

    
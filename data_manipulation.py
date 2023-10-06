import pandas as pd
from loguru import logger

# Class for data manipulation
class DataManipulation:
    # Function for initializing the class
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    # Function for checking if a file exists, return error if not
    def file_exists(self) -> bool:
        try:
            open(self.file_name)
        except FileNotFoundError:
            logger.error("File not found")
            return False
        logger.info("File found")
        return True

    # Function for reading csv file, but before needs to check if the file exists
    def read_csv(self) -> pd.DataFrame:
        if self.file_exists():
            logger.info("Reading CSV file")
            return pd.read_csv(self.file_name)
        
    # Function for dropping NaN values in pandas df
    def drop_nan(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.info("Dropping NaN values")
        return df.dropna()
    
    # Function for dropping duplicates in pandas df
    def drop_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.info("Dropping duplicates")
        return df.drop_duplicates()
    
    # Function for dropping columns in pandas df
    def drop_columns(self, df: pd.DataFrame, columns: list) -> pd.DataFrame:
        logger.info("Dropping columns")
        return df.drop(columns, axis=1)
    
    # Function for renaming columns in pandas df
    def rename_columns(self, df: pd.DataFrame, columns: dict) -> pd.DataFrame:
        logger.info("Renaming columns")
        return df.rename(columns=columns)
    
    # Function for changing column type in pandas df
    def change_column_type(self, df: pd.DataFrame, column: str, type: str) -> pd.DataFrame:
        logger.info("Changing column type")
        return df[column].astype(type)
    
    # Function for saving pandas df to csv file
    def save_csv(self, df: pd.DataFrame, file_name: str) -> None:
        logger.info("Saving CSV file")
        df.to_csv(file_name, index=False)
    

    

    
import pandas as pd
import logging


def read_csv(file_path):
    """
    Reads a CSV file and returns a pandas DataFrame.
    
    :param file_path: str, path to the CSV file
    :return: pd.DataFrame, DataFrame containing the data from the CSV file
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return None
    

def read_excel(file_path, sheet_name=0):
    """
    Reads an Excel file and returns a pandas DataFrame.
    
    :param file_path: str, path to the Excel file
    :param sheet_name: str or int, name or index of the sheet to read
    :return: pd.DataFrame, DataFrame containing the data from the specified sheet
    """
    try:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        return df
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return None
    

def read(file_path, **kwargs):
    """
    Reads data from a file and returns a pandas DataFrame.
    
    :param file_path: str, path to the file (CSV or Excel)
    :param kwargs: additional arguments for reading the file
    :return: pd.DataFrame, DataFrame containing the data from the file
    """
    try:
        logging.info(f"Reading file as csv")
        df = read_csv(file_path)
        return df
    except Exception as e:
        logging.error(f"Failed to read file as csv: {e}")
        try:
            logging.info(f"Reading file as excel")
            df = read_excel(file_path, **kwargs)
            return df
        except Exception as e:
            logging.error(f"Failed to read file as excel: {e}")
            return None

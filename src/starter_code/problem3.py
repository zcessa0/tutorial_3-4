# Problem 3: Delete unnecessary columns
from pathlib import Path

import pandas as pd


def create_dataframe(csv_file):
    """ Creates, prints and returns a pandas dataframe containing data from a csv file

    Args:
        csv_file: The raw data in csv format

    Returns:
        df: A pandas dataframe with the data

    """
    df = pd.read_csv(csv_file)
    pd.set_option('display.max_rows', df.shape[0] + 1)
    pd.set_option('display.max_columns', df.shape[1] + 1)
    # print("\nDataFrame contents:\n", df)
    return df


def print_df_information(df):
    """ Prints information that the describes the contents of the DataFrame.

    Args:
        df: A pandas dataframe containing the data
    """
    # Print the number of rows and columns in the DataFrame using `.shape`
    print("\nNumber of rows and columns:\n")
    print(df.shape)  # Add your code inside the brackets

    # Print the first 7 rows of data using `.head()` and the last 6 rows using `.tail()`
    print("\nFirst 7 rows:\n")
    print(df.head(7))  # Add your code inside the brackets
    print("\nLast 6 rows:\n")
    print(df.tail(6))  # Add your code inside the brackets

    #  Print the column labels using `.info()` or `.columns`.
    #  Are there any columns that you don't think will be needed to answer the questions?
    print("\nColumn labels:\n")
    print(df.info())  # Add your code inside the brackets

    # Print the column data types using `.info()` or `.dtypes`
    print("\nColumn data types:\n")
    print(df.dtypes)  # Add your code inside the brackets

    # Print general statistics using `.describe()`
    # Why are some columns not shown in the output?
    print("\nStatistics:\n")
    print(df.describe())  # Add your code inside the brackets


def prepare_data(df):
    """ Takes the raw data and prepares it for later use in the paralympics dashboard

       Args:
           df: The raw data in a pandas DataFrame

       Returns:
        df_prepared: A pandas DataFrame with the prepared data

       """
    # 1. Drop the list of named columns `['Events', 'Sports', 'Countries'] and
    # assign the result to a new variable named df_prepared
    df_prepared = ''  # Add code and delete the ''
    return df_prepared


if __name__ == '__main__':
    raw_data_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    raw_df = create_dataframe(raw_data_file)
    print_df_information(raw_df)

    # Code to run problem 3 solution
    print("\nColumns before deletion:\n", raw_df.columns)
    dropped_cols_df = prepare_data(raw_df)
    print("\nColumns after deletion:\n", dropped_cols_df.columns)

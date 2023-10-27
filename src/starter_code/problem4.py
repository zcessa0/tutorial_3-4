# Problem 4: Dealing with missing values
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
    print("\nNumber of rows and columns:\n")
    print(df.shape)
    print("\nFirst 7 rows:\n")
    print(df.head(7))
    print("\nLast 6 rows:\n")
    print(df.tail(6))
    print("\nColumn labels:\n")
    print(df.columns)
    print("\nColumn labels, datatypes and value counts:\n")
    print(df.info())
    print("\nColumn data types:\n")
    print(df.dtypes)
    print("\nGeneral Statistics:\n")
    print(df.describe())


def prepare_data(df):
    """ Takes the raw data and prepares it for later use in the paralympics dashboard

       Args:
           df: The raw data in a pandas DataFrame

       Returns:
        df_prepared: A pandas DataFrame with the prepared data

       """
    # Drop the list of named columns `['Events', 'Sports', 'Countries'] & assign to a new variable named df_prepared
    df_prepared = df.drop(['Events', 'Sports', 'Countries'], axis=1)

    # 3.1 Drop rows where there is NaN in the 'Participants M' or 'Participants F' columns
    # Use `dropna` and specify to only remove  with null/Nan in the Participants (M) and Participants (F) columns
    # The general syntax is: df.dropna(subset=['AColName', 'AnotherColName'])
    # Remember: assign the result to a new DataFrame, or use the `inplace=True` attribute

    # 3.2 Replace the NaN in Type column with 'Winter'
    # The general syntax is: df.fillna({'ColName': 'ValueToReplaceNull'})
    # Remember: assign the result to a new DataFrame, or use the `inplace=True` attribute

    return df_prepared


if __name__ == '__main__':
    raw_data_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    raw_df = create_dataframe(raw_data_file)
    # print_df_information(raw_df)
    dropped_cols_df = prepare_data(raw_df)

    # Problem 4
    # 1. Print the missing values in the DataFrame using .isna() or isnnull(). 'True' indicates a missing value.
    print()  # add code inside the print

    # 2. Create a dataframe named `missing_rows` with only the rows that contain any missing values
    missing_rows = ''  # Add code here, delete the ''
    print(missing_rows)

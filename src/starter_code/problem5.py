# Problem 5: Dealing with inconsistent values for categorical data
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
    # Drop the list of named columns `['Events', 'Sports', 'Countries'] and
    # assign the result to a new variable named df_prepared
    df_prepared = df.drop(['Events', 'Sports', 'Countries'], axis=1)
    # Drop rows where there is NaN in the 'Participants M' or 'Participants F' columns
    df_prepared.dropna(subset=['Participants (M)', 'Participants (F)'], inplace=True)
    # Replace the NaN in Type column with 'Winter'
    df_prepared.fillna({'Type': 'Winter'}, inplace=True)

    # 2. Remove the whitespace from the Type values using `str.strip()`
    # General syntax: df['ColName'] = df['ColName'].str.strip()
    df_prepared['Type'] = df_prepared['Type'].str.strip()


    return df_prepared


if __name__ == '__main__':
    raw_data_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    raw_df = create_dataframe(raw_data_file)
    # print_df_information(raw_df)
    nulls_fixed_df = prepare_data(raw_df)

    # Problem 4 solution
    # NB: The solution won't run in this file as the issues have been addressed in prepare_data and the DataFrame on
    # line 73 is renamed from dropped_cols_df to nulls_fixed_df
    # Print the number of missing values in the DataFrame
    # print(dropped_cols_df.isna())
    # Create a dataframe with only the rows that contain any missing values
    # missing_rows = dropped_cols_df[dropped_cols_df.isna().any(axis=1)]
    # print("\nRows with nulls:\n", missing_rows)

    # Problem 5 code
    # Print the unique values for the Type column.
    # The general syntax is: df['ColName'].unique()
    print()

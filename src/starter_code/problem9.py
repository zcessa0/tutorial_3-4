# Problem 9: Identifying outliers
from pathlib import Path

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd


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
    print("\nRows with nulls:\n")
    nulls_df = df[df.isna().any(axis=1)]
    print(nulls_df)
    print("\nThe unique values for the Type column\n", df['Type'].unique())


if __name__ == '__main__':
    prepared_data_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_prepared.csv')
    # Parse the dates to strings when the data is loaded to the DataFrame
    prepared_df = pd.read_csv(prepared_data_file, parse_dates=['Start', 'End'], dtype={'Year': str})

    # 1. Create a box plot and show it

    # 2. Modify the box plot to create separate plots for each variable using the argunent submplots=True

    # 3. Save the image to file in the data directory


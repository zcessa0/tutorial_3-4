# Problem 10: Timeseries data
from pathlib import Path

import matplotlib

matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt


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
    # Parse the dates as a date in the format of Year when the data is loaded to the DataFrame
    prepared_df = pd.read_csv(prepared_data_file, parse_dates=['Start', 'End'], dtype={'Year': str})

    # 1. Create a line chart using pd.DataFrame.plot
    #prepared_df.plot(x="Start", y="Participants")
    #plt.show()

    # 2. Group the data by Type and display the chart
    prepared_df.groupby("Type").plot(x="Start", y="Participants", xticks=prepared_df['Start'])
    plt.show()
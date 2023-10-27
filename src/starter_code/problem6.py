# Problem 6: Combining data sets
from pathlib import Path

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


def prepare_data(df, df2):
    """ Takes the raw data and prepares it for later use in the paralympics dashboard

        TODO: The arguments could be given more meaningful names than df, df2...

       Args:
           df: The raw paralympics data in a pandas DataFrame
           df2: The NOC code data in a pandas DataFrame

       Returns:
        df_prepared: A pandas DataFrame with the prepared data

       """
    # Drop the list of named columns `['Events', 'Sports', 'Countries']
    df_dropcols = df.drop(['Events', 'Sports', 'Countries'], axis=1)
    # Drop rows where there is NaN in the 'Participants M' or 'Participants F' columns
    df_dropnans = df_dropcols.dropna(subset=['Participants (M)', 'Participants (F)'])
    # Replace the NaN in Type column with 'Winter'
    df_fillnans = df_dropnans.fillna({'Type': 'Winter'})
    # Remove the whitespace from the Type values using `str.strip()`
    df_fillnans['Type'] = df_fillnans['Type'].str.strip()

    # 2. Merge the DataFrames using a left merge. See the tutorial instructions for details.
    df_merged = ''

    # 3. Drop either the Country or region column (see problem 3)

    df_prepared = df_merged

    return df_prepared


if __name__ == '__main__':
    raw_data_events = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    events_df = pd.read_csv(raw_data_events)
    pd.set_option('display.max_rows', events_df.shape[0] + 1)
    pd.set_option('display.max_columns', events_df.shape[1] + 1)

    # 1. Create a data frame with the 'NOC' and 'region' columns from 'data/noc_regions.csv'
    # Hint: Path(__file__).parent.parent.joinpath('data', 'noc_regions.csv') to reference the file
    # Hint: Use the `usecols=['Col','Col2']` attribute in `pd.read_csv`

    # 4. Create the merged dataframe by passing df (events_df) and df2 (noc_df) to `prepare_data(df, f1)`

    # 5. Print any rows in the merged DataFrame that have NaNs

    # 6. Print all rows of the NOC DataFrame

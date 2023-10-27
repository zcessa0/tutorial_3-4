# Problem 8: Save the prepared dataset to a csv file
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

    The raw data is transformed in a series of steps and the output is saved to a csv file and returned as a DataFrame.

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
    # Create the merged dataframe
    df_merged = df_fillnans.merge(df2, how='left', left_on='Country', right_on='region')
    df_merged = df_merged.drop(['region'], axis=1)
    df_merged['NOC'] = df_merged['NOC'].mask(df_merged['Country'] == 'Great Britain', 'GBR')
    df_merged['NOC'] = df_merged['NOC'].mask(df_merged['Country'] == 'Republic of Korea', 'KOR')

    # Add the year to the Start and End columns to create a full date as a string.
    # TODO: Consider if there is a case where the dates span year end e.g. December to January)
    df_merged["Start"] = df_merged["Start"] + '-' + df_merged["Year"].astype(str)
    df_merged["End"] = df_merged["End"] + '-' + df_merged["Year"].astype(str)

    # Change the column datatype for Start and End from string to date-time format
    df_merged['Start'] = pd.to_datetime(df_merged['Start'], format='%d-%b-%Y')
    df_merged['End'] = pd.to_datetime(df_merged['End'], format='%d-%b-%Y')

    # Add a duration column to the DataFrame
    df_merged['Duration'] = df_merged['End'] - df_merged['Start']
    # Change the data type of df_merged['Duration'] to int
    df_merged['Duration'] = df_merged['Duration'].dt.days

    df_prepared = df_merged

    # 1. Save the prepared dataframe to a .csv file
    # Hint: Define the file location using Pathlib.path
    # Hint: To avoid saving the pandas index column, use the `index=False` argument

    return df_prepared


if __name__ == '__main__':
    raw_data_events = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    events_df = pd.read_csv(raw_data_events)
    pd.set_option('display.max_rows', events_df.shape[0] + 1)
    pd.set_option('display.max_columns', events_df.shape[1] + 1)
    raw_data_noc = Path(__file__).parent.parent.joinpath('data', 'noc_regions.csv')
    cols = ['NOC', 'region']
    noc_df = pd.read_csv(raw_data_noc, usecols=cols)
    prepare_data(df=events_df, df2=noc_df)

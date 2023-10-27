# Problem 7: Compute new data
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
    # Create the merged dataframe
    df_merged = df_fillnans.merge(df2, how='left', left_on='Country', right_on='region')
    df_merged = df_merged.drop(['region'], axis=1)
    df_merged['NOC'] = df_merged['NOC'].mask(df_merged['Country'] == 'Great Britain', 'GBR')
    df_merged['NOC'] = df_merged['NOC'].mask(df_merged['Country'] == 'Republic of Korea', 'KOR')

    # 3. Add the year to the Start and End columns to create a full date as a string.
    # Year is int and Start/End are strings. To combine these as a string, convert the Year to string.
    # TODO: Consider if there is a case where the dates span year end e.g. December to January)
    df_merged["Start"] = + df_merged["Start"] + '-' + df_merged["Year"].astype(str)
        # Add code to make df_merged["End"] a string format date

    # 4. Change the datatype for Start and End from string to date-time format.
    # Pandas to_datetime handles most date formats so the following should work without using the `format=` argument.
    # 'Start' is given below.
    df_merged['Start'] = pd.to_datetime(df_merged['Start'], format='%d-%b-%Y')
    # df_merged['Start'] = pd.to_datetime(df_merged['Start'])  # This should also work
         # Add the code change the datatype for 'End' from string to date-time format.

    df_merged['Start'] = pd.to_datetime(df_merged['Start'], format='%d-%b-%Y')
    # df['Start'] = pd.to_datetime(df['Start'])  # Should also work without `format=`

    # 5. Add a duration column to the DataFrame that is the difference in days between the
    # start and end dates. The datatype should be integer.

    # The output of the above is in timedelta format, this may not suit your needs
    # Change the data type of df_merged['Duration'] to int using .dt.days

    df_prepared = df_merged
    return df_prepared


if __name__ == '__main__':
    raw_data_events = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    events_df = pd.read_csv(raw_data_events)
    pd.set_option('display.max_rows', events_df.shape[0] + 1)
    pd.set_option('display.max_columns', events_df.shape[1] + 1)
    raw_data_noc = Path(__file__).parent.parent.joinpath('data', 'noc_regions.csv')
    cols = ['NOC', 'region']
    noc_df = pd.read_csv(raw_data_noc, usecols=cols)
    merged_df = prepare_data(df=events_df, df2=noc_df)

    # 1. Print the data types of the ['Year', 'Start', 'End'] columns

    # 2. Check the format of the values in  `['Year', 'Start', 'End']` by printing a couple of rows

    # After completing step 3, run the code for 1 and 2 again to check the datatypes and values of Start and End

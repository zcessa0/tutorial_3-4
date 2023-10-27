from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


if __name__ == '__main__':
    prepared_csv_filepath = Path(__file__).parent.parent.joinpath('data', 'paralympics_prepared.csv')
    # Parse the dates as a date in the format of Year when the data is loaded to the DataFrame
    df_prepared = pd.read_csv(prepared_csv_filepath, parse_dates=['Start', 'End'], dtype={'Year': str})

    # Add code here to create the box plot

from pathlib import Path


def create_dataframe(csv_file):
    """ Creates, prints and returns a pandas dataframe containing data from a csv file

    Args:
        csv_file: The raw data in csv format

    Returns:
        df: A pandas dataframe with the data

    """
    # 1. Complete the code to create a variable called 'df' that is a pandas dataframe that reads its contents from the
    # csv file.
    # Use pandas.read_csv https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

    # Uncomment the 2 lines of code below to set the pandas display options to show all rows and columns of the dataset
    # Otherwise, by default pandas will only print as many columns and rows as can be displayed in your terminal window

    # pd.set_option('display.max_rows', df.shape[0] + 1)
    # pd.set_option('display.max_columns', df.shape[1] + 1)

    # 2. Add a line of code to using Python print() to print the dataframe contents

    # 4. Complete the line of code to return the dataframe
    return


if __name__ == '__main__':
    # Use Pathlib.Path to read a file using the location relative to this file
    raw_data_file = Path(__file__).parent.parent.joinpath('data', 'paralympics_raw.csv')
    # Call the create_dataframe function, passing the csv file as argument
    df_raw = create_dataframe(raw_data_file)

import pandas as pd

from get_remote_data import get_df


def get_data_column(data_col) -> int:
    """
        Returns a number corresponding with the number of the row in the CSV correlated with the data

        :param data_col: The data column to return
        :type data_col: string
        :rtype: int
        """
    if data_col == "total_cases":
        return 4
    elif data_col == "total_vaccinations":
        return 34
    elif data_col == "total_deaths":
        return 7


def filter_data(start_date, end_date, country, data_col, df):
    """
        Filters a data frame within date boundaries for selected data column from a country

        :param start_date: Start date to filter by
        :type start_date: tuple[int, int, int]
        :param end_date: End date to filter by
        :type end_date: tuple[int, int, int]
        :param country: Country name to filter by
        :type country: string
        :param data_col: Name of column to filter by
        :type data_col: string
        :param df: The data frame to filter from
        :type df: dataframe
    """
    start_datetime = pd.to_datetime(start_date, dayfirst=True)
    end_datetime = pd.to_datetime(end_date, dayfirst=True)

    list_values = df.loc[(df['date'].between(start_datetime, end_datetime) & (df['location'] == country))] \
        .sort_values(by='date').values.tolist()

    dates: list = []
    data: list = []
    column = get_data_column(data_col)

    for row in list_values:
        timestamp = row[3]
        dates.append(timestamp.strftime("%d-%m-%Y"))
        data.append(row[column])
    return dates, data

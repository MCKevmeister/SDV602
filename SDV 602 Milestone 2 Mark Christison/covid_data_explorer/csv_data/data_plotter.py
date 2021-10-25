import pandas as pd

from get_remote_data import get_df


def get_data_column(data_col) -> int:
    if data_col == "total_cases":
        return 4
    elif data_col == "total_vaccinations":
        return 34
    elif data_col == "total_deaths":
        return 7


def filter_data(start_date, end_date, country, data_col, df):
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


if __name__ == '__main__':
    print("starting getting data frame")
    data_frame = get_df()
    print("got dataframe")
    print(filter_data('1/3/21', '2/3/21', 'New Zealand', 'total_cases', data_frame))
    print(filter_data('2/4/21', '20/4/21', "New Zealand", 'total_vaccinations', data_frame))


import pandas as pd
from shared_data import data_source


def get_df():
    """
        Gets the CSV file and converts it into a pandas data frame
    """
    data_source.clear()
    external_data = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', parse_dates=[3],
                                dayfirst=True)
    data_source.append(external_data.values.tolist())


# Below function was previously used to create a list of countries when using a CSV file.
# No longer necessary since the requirements require using remote data and country list was made
# def get_countries_from_csv():
#     with open('owid-covid-data.csv', newline='') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         for row in csv_reader:
#             if row[2] not in countries:
#                 countries.append(row[2])

# def print_first_row():
#     with open('owid-covid-data.csv', newline='') as csv_file:
#         reader = csv.reader(csv_file)
#         # for row in reader:
#         #     print(" ".join(row))
#         print(next(reader))


# if __name__ == '__main__':
#     print_first_row()

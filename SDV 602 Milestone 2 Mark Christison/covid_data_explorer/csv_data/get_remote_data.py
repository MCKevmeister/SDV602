import pandas as pd


# Below function was previously used to create a list of countries when using a CSV file. No longer necessary

# def get_countries():
#     with open('owid-covid-data.csv', newline='') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         for row in csv_reader:
#             if row[0] not in countries:
#                 countries.append(row[0])

def get_df():
    return pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv', parse_dates=[3], dayfirst=True)


if __name__ == '__main__':
    print(get_df())

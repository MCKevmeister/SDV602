import csv
import os

countries = []


def get_countries():
    with open('csv_data/owid-covid-data.csv', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # countries_list = []
        # countries_list = [row[0] for row in csv_reader if row[0] not in countries_list]
        # countries = countries_list
        for row in csv_reader:
            if row[0] not in countries:
                countries.append(row[0])


if __name__ == '__main__':
    get_countries()

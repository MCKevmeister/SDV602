import csv

countries = []


def get_countries():
    with open('owid-covid-data.csv', newline='') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] not in countries:
                countries.append(row[0])


if __name__ == '__main__':
    get_countries()

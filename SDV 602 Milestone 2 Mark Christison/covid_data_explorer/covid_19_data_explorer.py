from data_plotter import parse_data
from views.main import main_view
from csv_data_reader import get_countries


if __name__ == '__main__':
    get_countries()
    main_view()

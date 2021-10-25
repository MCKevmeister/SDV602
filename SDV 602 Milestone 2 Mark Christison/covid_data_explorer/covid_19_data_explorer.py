from get_remote_data import get_df
from views.main import main_view

global data_frame

if __name__ == '__main__':
    data_frame = get_df()
    main_view()

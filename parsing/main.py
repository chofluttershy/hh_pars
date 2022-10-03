import PySimpleGUI as sg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def read_table():
    sg.set_options(auto_size_buttons=True)
    filename = sg.popup_get_file(
        'Dataset to read',
        title='Dataset to read',
        no_window=True,
        file_types=(("CSV Files", "*.csv"), ("Text Files", "*.txt")))
    if filename == '':
        return

    data = []
    header_list = []
    colnames_prompt = 'Yes'
    nan_prompt = 'No'

    if filename is not None:
        fn = filename.split('/')[-1]
        try:
            if colnames_prompt == 'Yes':
                df = pd.read_csv(filename, sep=',', engine='python')

                header_list = list(df.columns)

                data = df[1:].values.tolist()
            else:
                df = pd.read_csv(filename, sep=',', engine='python', header=None)

                header_list = ['column' + str(x) for x in range(len(df.iloc[0]))]
                df.columns = header_list

                data = df.values.tolist()
            # выбрасываем Nan
            if nan_prompt == 'Yes':
                df = df.dropna()

            return (df, data, header_list, fn)

        except:
            sg.popup_error('Error reading file')
            return


def show_table(data, header_list, fn):
    layout = [
        [sg.Table(values=data,
                  headings=header_list,
                  font='Helvetica',
                  pad=(25, 25),
                  display_row_numbers=False,
                  auto_size_columns=True,
                  num_rows=min(25, len(data)))]
    ]

    window = sg.Window(fn, layout, grab_anywhere=False)
    event, values = window.read()
    window.close()


def main():
    df, data, header_list, fn = read_table()

    show_prompt = 'Yes'
    if show_prompt == 'Yes':
        show_table(data, header_list, fn)

    # Show stats?
    #stats_prompt = sg.popup_yes_no('Show the descriptive stats?')
    # if stats_prompt == 'Yes':
    #     show_stats(df)
    #
    # # Show a plot?
    # plot_prompt = sg.popup_yes_no('Show a scatter plot?')
    # if plot_prompt == 'Yes':
    #     plot_fig(df)


if __name__ == '__main__':
    main()
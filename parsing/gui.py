import PySimpleGUI as sg
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# Дать макет строки графического интерфейса
layout = [[sg.Text('Enter a Number')],
          [sg.Input()],
          [sg.OK()]]

#sg.ChangeLookAndFeel("White")

 # Создать графический интерфейс
#event, (number,) = sg.Window('Enter a number example').Layout(layout).Read()

window = sg.Window('Pattern 2B', layout)

while True:  # Event Loop
    event, number = window.read()
    print(event, number)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(number['-IN-'])

window.close()

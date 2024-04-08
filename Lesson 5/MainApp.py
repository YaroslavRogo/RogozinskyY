import tkinter
from tkinter import Tk, Button, filedialog
from ErrorWindow import ErrorWindow
import config

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import pandas as pd

class MainApp(Tk):
    # Класс создания основного окна
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        self.count = 3
        self.button1 = Tk.Button(self, text='Выбрать файл',
                             width=25, command = self.new_window)
        self.button1.pack()
        self.button2 = Tk.Button(self, text='Визуализация',
                             width=25, command=self.new_info_window)
        self.button2.pack()

        position = {"relx": 0.6, "rely": 0.01}
        self.button1.place(relx=0.1, rely=0.01)
        self.button2.place(relx=0.1, rely=0.011)
        item = 0

    def __init__(self, *arg, **kwarg):
       super().__init__(*arg, **kwarg)

       self.quitButton = Tk.Button(self, text='Quit', width=25, command=self.close_windows)
       self.quitButton.pack()


    def close_windows(self):
            self.destroy()


def main():
  app = MainApp()
  app.title("Окно визуализации")
  app.geometry('300x200+200+100')
  app.mainloop()
  if __name__ == '__main__':
    main()
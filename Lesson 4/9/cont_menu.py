import tkinter as tk
from tkinter import Menu

class MainWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.grid(row=0, column=0)

        self.principal = tk.DoubleVar()
        self.principal.set(1000.0)
        self.rate = tk.DoubleVar()
        self.rate.set(5.0)
        self.years = tk.IntVar()
        self.years.set(1)  # Начальное значение years
        self.amount = tk.StringVar()

        principalLabel = tk.Label(self, text="Principal $:", anchor=tk.W, underline=0)
        principalScale = tk.Scale(self, variable=self.principal, command=self.updateUi, from_=100, to=10000000, resolution=100, orient=tk.HORIZONTAL)
        rateLabel = tk.Label(self, text="Rate %:", underline=0, anchor=tk.W)
        rateScale = tk.Scale(self, variable=self.rate, command=self.updateUi, from_=1, to=50, orient=tk.HORIZONTAL)
        yearsLabel = tk.Label(self, text="Years:", underline=0, anchor=tk.W)
        self.yearsScale = tk.Scale(self, variable=self.years, command=self.updateUi, from_=1, to=50, orient=tk.HORIZONTAL)
        amountLabel = tk.Label(self, text="Amount: $", anchor=tk.W)
        actualAmountLabel = tk.Label(self, textvariable=self.amount, relief=tk.SUNKEN, anchor=tk.E)

        principalLabel.grid(row=0, column=0, padx=2, pady=2, sticky=tk.W)
        principalScale.grid(row=0, column=1, padx=2, pady=2, sticky=tk.EW)
        rateLabel.grid(row=1, column=0, padx=2, pady=2, sticky=tk.W)
        rateScale.grid(row=1, column=1, padx=2, pady=2, sticky=tk.EW)
        yearsLabel.grid(row=2, column=0, padx=2, pady=2, sticky=tk.W)
        self.yearsScale.grid(row=2, column=1, padx=2, pady=2, sticky=tk.EW)
        amountLabel.grid(row=3, column=0, padx=2, pady=2, sticky=tk.W)
        actualAmountLabel.grid(row=3, column=1, padx=2, pady=2, sticky=tk.EW)

        principalScale.focus_set()
        self.updateUi()

    def updateUi(self, *ignore):
        amount = self.principal.get() * ((1 + (self.rate.get() / 100.0)) ** self.years.get())
        self.amount.set("{0:.2f}".format(amount))

    def quit(self, event=None):
        self.parent.destroy()


application = tk.Tk()

#!
def increase_years():
    years = window.years.get()
    window.years.set(years + 1)

def decrease_years():
    years = window.years.get()
    if years > 1:
        window.years.set(years - 1)

window = MainWindow(application)

mainmenu = Menu(application)
application.config(menu=mainmenu)

filemenu = Menu(mainmenu, tearoff=0)
filemenu.add_command(label="Выход", command=window.quit)
mainmenu.add_cascade(label="Файл", menu=filemenu)

popup_menu = Menu(window, tearoff=0)
popup_menu.add_command(label="Увеличить Years", command=increase_years)
popup_menu.add_command(label="Уменьшить Years", command=decrease_years)

window.yearsScale.bind("<Button-3>", lambda event: popup_menu.post(event.x_root, event.y_root))

window.pack()
application.mainloop()
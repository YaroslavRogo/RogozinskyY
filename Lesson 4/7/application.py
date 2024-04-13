import tkinter as tk
from MainWindow import MainWindow
import os
import sys


application = tk.Tk()

path = os.path.join(os.path.dirname(__file__), "images/")

if sys.platform.startswith("win"):
    icon = os.path.join(path, "interest.ico")
else:
    icon = "@" + os.path.join(path, "interest.xbm")

application.iconbitmap(icon)
application.title("Interest")
window = MainWindow(application)

application.protocol("WM_DELETE_WINDOW", window.quit)
application.mainloop()
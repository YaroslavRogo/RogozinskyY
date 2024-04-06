from tkinter import *
from tkinter import Toplevel, Button, Label

class Func():
  def __init__(self, root, label):
    self.top = Toplevel(root)
    self.button_top_level = Button(self.top, text='Нажми', command=lambda: label.config(text='Текст из модального окна')).pack()
    self.top.grab_set()
    self.top.focus_set()
    self.top.wait_window()

root = Tk()
class ErrorWindow():
    def quit(event=None) -> None:
        root.destroy()

        mainmenu = Menu(root)
        root.config(menu=mainmenu)

        filemenu = Menu(mainmenu, tearoff=0)
        filemenu.add_command(label="Открыть...")
        filemenu.add_command(label="Новый")
        filemenu.add_command(label="Сохранить...")
        filemenu.add_separator()
        filemenu.add_command(label="Выход", command=quit)

        helpmenu = Menu(mainmenu, tearoff=0)

        helpmenu2 = Menu(helpmenu, tearoff=0)
        helpmenu2.add_command(label="Локальная справка")
        helpmenu2.add_command(label="На сайте")

        helpmenu.add_cascade(label="Помощь", menu=helpmenu2)
        helpmenu.add_command(label="О программе")

        mainmenu.add_cascade(label="Файл", menu=filemenu)
        mainmenu.add_cascade(label="Справка", menu=helpmenu)

        root.mainloop()

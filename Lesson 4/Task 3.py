from tkinter import *

root = Tk()

def myClick():
#Обработчик событий при нажатии кнопки
    myLabel = Label(root, text="Нажата кнопка!")
    myLabel.pack()
myButton = Button(root, text = "Нажми", command=myClick, fg="blue", bg="#ffffff")
myButton.pack()
root.mainloop()
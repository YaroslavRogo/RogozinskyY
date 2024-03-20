class Bud
    def __init__(self, a, b): # на вход даётся час и минута
     self.__a = a
     self.__b = b


from tkinter import *
root = Tk()
def myClick():       #Обработчик событий при нажатии кнопки
    myLabel = Label(root, text="Look! I clicked a Button!")
    myLabel.pack()
myButton = Button(root, text = "Click Me!", command=myClick, fg="blue", bg="#ffffff")
myButton.pack()
root.mainloop()
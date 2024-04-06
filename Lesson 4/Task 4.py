from tkinter import *
root = Tk()
e = Entry(root, width=50, text = "Введите ваше имя", bg='blue', fg = "white", borderwidth = 5)
e.pack()
e.insert(0, "")

def myClick():

   hello = "Привет введённые данные: " + e.get()
   myLabel = Label(root, text=hello)
   myLabel.pack()
myButton = Button(root, text = "Нажмите", command=myClick, fg="blue", bg="#ffffff")
myButton.pack()
root.mainloop()
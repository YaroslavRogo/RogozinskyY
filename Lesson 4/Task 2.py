import tkinter as tk

root = tk.Tk()

Person = input()

myLabel = tk.Label(root)
myLabel.grid(row=0, column=0)

myButton1 = tk.Button(root, text="Hello World!", width = 30)
myButton1.grid(row=0, column=0)

myButton2 = tk.Button(root, width = 30)
myButton2.grid(row=1, column=0)

myButton3 = tk.Button(root, width = 30)
myButton3.grid(row=0, column=2)

myButton4 = tk.Button(root, text="My Name Is " + Person, width = 30)
myButton4.grid(row=1, column=2)


root.mainloop()
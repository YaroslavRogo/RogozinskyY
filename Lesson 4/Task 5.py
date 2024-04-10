import tkinter as tk


class Click(tk.Tk):
    def __init__(self):
        super().__init__()
        self.e = tk.Entry(self, width=42, bg='white', fg="black", borderwidth=5)

        self.e.pack()

        self.result = tk.StringVar(self)

        self.button0 = tk.Button(self, text='0', width=10, height=3, command=lambda: self.button_click('0'))
        self.button0.place(relx=0.06, rely=0.54)

        self.button1 = tk.Button(self, text='1', width=10, height=3, command=lambda: self.button_click('1'))
        self.button1.place(relx=0.06, rely=0.39)

        self.button2 = tk.Button(self, text='2', width=10, height=3, command=lambda: self.button_click('2'))
        self.button2.place(relx=0.37, rely=0.39)

        self.button3 = tk.Button(self, text='3', width=10, height=3, command=lambda: self.button_click('3'))
        self.button3.place(relx=0.67, rely=0.39)

        self.button4 = tk.Button(self, text='4', width=10, height=3, command=lambda: self.button_click('4'))
        self.button4.place(relx=0.06, rely=0.24)

        self.button5 = tk.Button(self, text='5', width=10, height=3, command=lambda: self.button_click('5'))
        self.button5.place(relx=0.37, rely=0.24)

        self.button6 = tk.Button(self, text='6', width=10, height=3, command=lambda: self.button_click('6'))
        self.button6.place(relx=0.67, rely=0.24)

        self.button7 = tk.Button(self, text='7', width=10, height=3, command=lambda: self.button_click('7'))
        self.button7.place(relx=0.06, rely=0.09)

        self.button8 = tk.Button(self, text='8', width=10, height=3, command=lambda: self.button_click('8'))
        self.button8.place(relx=0.37, rely=0.09)

        self.button9 = tk.Button(self, text='9', width=10, height=3, command=lambda: self.button_click('9'))
        self.button9.place(relx=0.67, rely=0.09)

        self.button_clear = tk.Button(self, text='Очистить', width=23, height=3, command=self.clear_entry)
        self.button_clear.place(relx=0.37, rely=0.54)

        self.button_add = tk.Button(self, text='+', width=10, height=3, command=lambda: self.save_number('+'))
        self.button_add.place(relx=0.06, rely=0.69)

        self.button_subtract = tk.Button(self, text='-', width=10, height=3, command=lambda: self.save_number('-'))
        self.button_subtract.place(relx=0.06, rely=0.83)

        self.button_multiply = tk.Button(self, text='*', width=10, height=3, command=lambda: self.save_number('*'))
        self.button_multiply.place(relx=0.37, rely=0.83)

        self.button_divide = tk.Button(self, text='/', width=10, height=3, command=lambda: self.save_number('/'))
        self.button_divide.place(relx=0.67, rely=0.83)

        self.button_equal = tk.Button(self, text='=', width=23, height=3, command=self.calculate_result)
        self.button_equal.place(relx=0.37, rely=0.69)

        self.first_number = ''
        self.math = ''

    def button_click(self, number):
        self.e.insert(tk.END,  number)


    def save_number(self, value):
        self.first_number = self.e.get()
        self.math = value
        self.e.delete(0, tk.END)

    def calculate_result(self):
        second_number = self.e.get()
        self.e.delete(0, tk.END)

        if self.math == '+':
            result = float(self.first_number) + float(second_number)
        elif self.math == '-':
            result = float(self.first_number) - float(second_number)
        elif self.math == '*':
            result = float(self.first_number) * float(second_number)
        elif self.math == '/':
            result = float(self.first_number) / float(second_number)


        self.e.insert(tk.END, str(result))

    def clear_entry(self):
        self.e.delete(0, tk.END)


click = Click()
click.title("Калькулятор")
click.geometry("300x500")
click.resizable(False, False)
click.mainloop()
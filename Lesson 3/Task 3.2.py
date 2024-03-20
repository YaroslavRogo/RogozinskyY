class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + " села.")

    def roll_over(self):
        print(self.name + " перекатывается.")

my_dog = Dog('willie', 6)
print("Имя собаки:", my_dog.name)
print("Возраст собаки:", my_dog.age)

my_dog.sit()
my_dog.roll_over()

my_dog2 = Dog('lucy', 3)
print("Имя собаки:", my_dog2.name)
print("Возраст собаки:", my_dog2.age)

my_dog2.sit()
my_dog2.roll_over()
from self import self

class Nikola:
     __slots__ = ('__name' , '__age' )

     def __init__(self,name,age):
         self.__name = "Николай"
         self.__age = 0
         if name == "Николай":
             print("Николай", age)
         if name != "Николай":
            print(f'Я не {name}, а Николай')

     #def __get__(self,name,age):
        # return self
         #return name.__dict__[self.__name]

     #def __set__(self, name, age):
         #if name == "Николай":
            #name = self.__name
         #return name.__dict__[self.__name]


Person1 = Nikola("Николай",18)
Person2 = Nikola("Игорь",32)
print(Person1.name)
print(Person2.name)
Person1.surname = 'Петров'
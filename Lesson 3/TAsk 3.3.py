from self import self


class House:
    def  __init__(self, _area, _price):
        self._area = _area
        self._price = _price

    def final_price(self, discount):
       return self._price * (100 - discount)/100

class SmallHouse(House):
    def  __init__(self, _area, _price, _obj_house = 40):
        super().__init__(_area, _price)
        self._obj_house = _obj_house
    def final_price(self, discount):
       return self._price * (100 - discount)/100

class Human:
    default_name = 'Yaroslav'
    default_age = '19'

    def __init__(self, name = default_name, age = default_age):
        self.name = name
        self.age = age
        self.__money =0
        self.__house = None

    def info(self):
           print(self.name)
           print(self.age)
           print(self.__house)
           print(self.__money)

    @staticmethod
    def default_info():
        print(Human.default_name)
        print(Human.default_age)

    def __make_deal(self, price, house):

        self.__money = self.__money - price
        self.__house = house
    def earn_money(self, add_money):
        self.__money = self.__money + add_money

    def buy_house(self, house:House, discount):
        actual_price = house.final_price(discount)
        if self.__money <  actual_price:
            print('Денег на счету не хватает')
        else:
            self.__make_deal(actual_price, house)


Human.default_info()

human = Human()

human.info()

small_house = SmallHouse(50, 100000)

human.buy_house(small_house, 10)

human.earn_money(150000)

human.buy_house(small_house, 10)

human.info()


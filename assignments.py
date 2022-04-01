class Menu ():
    def _init_(self, mealType, foodName, allergen, price, servingSize):
        self.mealType = mealType
        self.foodName = foodName
        self.allergen = allergen
        self.price = price
        self.servingSize = servingSize
    def printMenu(self):
        print("Hi Kelvin!, Here's your menu: ")
        print(self.foodName, self.servingSize, self.allergen, self.price)

class User():
        firstName = 'Francis'
        lastName = 'Ball'
        title = ''
        age = 25
        dietType = 'vegan'

class menuTime ():
    breakfast = '09:00am - 10:00am'
    lunch = '12:00pm - 01:00pm'
    dinner = '05:00pm - 06:00pm'


class menuItem():
    name = 'Bread and Egg'
    servingSize = 'Medium'
    allergen ='wheat, soy, gluten, dairy'
    

class order():
    orderId = '0011'
    user = 'Caroline'
    menu = ''

Menu1= Menu('Breakfast', 'Quaker_oats', 'soy', 15.0, 'Medium')
Menu2= Menu('Lunch', 'Waakye', 'fish', 20.0, 'Medium')
Menu3= Menu('Dinner', 'Potato_salad', 'Dairy', 10.0, 'Large')
Menu1.printMenu()
Menu2.printMenu()
Menu3.printMenu()
#output: 
# Price: 2000
# Speed: 35mph
# Fuel: Full
# Mileage: 15mpg
# Tax: 0.12

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed

        #would these below be considered methods?
        self.fuel = "Full"
        self.mileage = 0

    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed) 
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage)
        return self

    def taxed_price(self):
        if self.price > 10000:
            print ".15"
        else: 
            print ".12"

car1 = Car(10001,0,0,0)
print car1.display_all().taxed_price()
# car2 = Car()
# car3 = Car()
# car4 = Car()
# car5 = Car()
# car6 = Car()


# class User(object):
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.logged = False
#         self.poopcount = 2
#         return self


#     def poop(self, poopcount):
#         self.poopcount += poopcount
#         return self
#         # return poopcount
       
# user1 = User("Anna Propas", "anna@anna.com")
# user2 = User("Patrick","patrick@gmail.com")
# print user1.name
# print user1.logged
# print user1.email
# print user2.poop(1).poop(1).poopcount.poop(2).poopcount
# print user2.poopcount
# print user2.name
# print user2.email
# print user2.email().name()

class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    
    def displayinfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self

    def ride(self):
        self.miles += 10
        print "riding dirty"
        print self.miles
        return self

    def reverse(self):
        print "beep beep beep"
        self.miles -= 5
        print self.miles
        return self

bike1 = Bike(100,100,10)
bike2 = Bike(200,200,10)
bike3 = Bike(300,300,10)
print bike1.ride().ride().ride().reverse().displayinfo()
print bike2.ride().ride().reverse().reverse().displayinfo()
print bike3.reverse().reverse().reverse().displayinfo()
class Ya_Product(object):
    def __init__(self, price, item_name, weight, brand, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = status
    
    def sell(self, sold):
        #changes status to sold
        if sold == "Yes" or "yeah" or "F yeah":
            self.status = "Sold"
        return self

    def tax(self, tax):
        # takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
        self.price += self.price*tax
        print "Price after tax: " + str(self.price)

        return self

    def returns(self):
        #takes reason for return as a parameter and changes status accordingly. If the item is being returned because it is defective, change status to "defective" and change price to 0. If it is being returned in the box, like new, mark it "for sale". If the box has been, opened, set the status to "used" and apply a 20% discount.

        return self

    def displayinfo(self):
        # show all product details.
        print "Price: " + str(self.price)
        print "Item Name: " + str(self.item_name) 
        print "Weight: " + str(self.weight)
        print "Brand: " + str(self.brand)
        print "Status: " + str(self.status)

        return self
    
product1 = Ya_Product(0,0,0,0,"For Sale")
print product1.displayinfo().tax(.12).sell("F yeah")
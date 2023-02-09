class bikeShop:
    def __init__(self,stock):
        self.stock=stock
    def displayBike(self):
        print("total bikes",self.stock)
    def  rentaforbike(self,q):

        if q<=0:
            print("enter the positive value or greater then zero")
        elif q>self.stock:
            print("enter the value(less then stock)")
        else:
            self.stock=self.stock-q
            print("total price",q*100)
            print("total bikes",self.stock)

while True:
    obj=bikeShop(100)
    uc=int(input('''
1 display stocks
2 Rent a bike
3 Exit
         '''))

    if uc==1:
        obj.displayBike()
    elif uc==2:
        n=int(input("enter the quantity:---"))
    else:
        break
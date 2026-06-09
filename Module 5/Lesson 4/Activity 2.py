class computer:
    def __init__(self) -> None:
        self.__maxprice=900
    def sell(self):
        print("Selling price is",self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice=price
c=computer()
c.sell()
c.__maxprice=1200
c.sell()
c.setmaxprice(1200)
c.sell()

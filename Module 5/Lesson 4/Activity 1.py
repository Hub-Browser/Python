class myclass:
    _privateVar=27
    def __privateMeth(self):
        print("This is a private method")
    def hello(self):
        print(myclass._privateVar)
obj=myclass()
obj.hello()
obj.__privateMeth()
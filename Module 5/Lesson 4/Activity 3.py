class point:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)
p=point(2,3)
print(p)
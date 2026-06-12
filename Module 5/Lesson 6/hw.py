romeDat=[
    ('M',1000),('CM',900),('D',500),('CD',400),('C',100),('XC',90),('L',50),('XL',40),('X',10),('IX',9),('V',5),('IV',4),('I',1)
]
class Roman:
    def roman(self,n):
        result=[]
        for rome, value in romeDat:
            while n>=value:
                result.append(rome)
                n-=value
        return "".join(result) 
toRoman=Roman()
while True:
    try:
        print(toRoman.roman(int(input("Enter the number to be converted:"))))
    except:
        print("Invalid input")
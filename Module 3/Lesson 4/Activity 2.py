try:
    num1,num2=eval(input("Enter 2 numbers seperated by comma:"))
    result=num1/num2
    print("Result:",result)

except ZeroDivisionError as error:
    print("ZeroDivisionError:",error)
except SyntaxError as syn:
    print("SyntaxError:",syn)
except:
    print("Wrong input")

else:
    print("No error")
finally:
    print("This code will run no matter what")
x=5
if type(x) is int:
    print("True")
else:
    print("False")
y=5.5
if type(y) is not float:
    print("true")
else:
    print("false")
a=20
b=20
if a is b:
    print("a and b have the same identity")
b=30
if a is not b:
    print("a and b have different identity")
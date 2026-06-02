import random as r
n=r.randint(8,14)
p=""
for i in range(n):
    c=r.randint(32,126)
    p+=chr(c)
print(p)
import random as r
n=r.randint(8,14)
p=""
for i in range(n):
    p+=chr(r.randint(32,126))
print(p)
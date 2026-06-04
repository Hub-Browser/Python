class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=parrot("Blu",10)
woo=parrot("Woo",15)
print(f"The name of the first parrot is {blu.name}. He is a {blu.species}. He is {blu.age} years old. ")
print(f"The name of the second parrot is {woo.name}. He is a {woo.species}. He is {woo.age} years old. ")
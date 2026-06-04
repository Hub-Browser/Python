class dog:
    animal="dog"
    def  __init__(self,breed,color) -> None:
        self.breed=breed
        self.color=color
ger=dog("german shepherd","black")
bul=dog("bulldog","brown")
print(f"The first {ger.animal} is a {ger.color} {ger.breed}.")
print(f"The second {bul.animal} is a {bul.color} {bul.breed}.")


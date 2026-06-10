class bangladesh:
    def capital(self):
        print("Dhaka is the capital of bangladesh")
    def lang(self):
        print("belgali is the native language")
    def type(self):
        print("Bangladesh is a developing country\n")

class USA:
    def capital(self):
        print("Washington D.C is the capital of USA")
    def lang(self):
        print("English is the native language")
    def type(self):
        print("USA is a developed country\n")

class Spain:
    def capital(self):
        print("Madrid is the capital of Spain")
    def lang(self):
        print("Spanish is the native language")
    def type(self):
        print("Spain is a developed country\n")

b=bangladesh()
u=USA()
s=Spain()
for country in b,u,s:
    country.capital()
    country.lang()
    country.type()


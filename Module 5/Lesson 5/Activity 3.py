class Japan:
    def capital(self):
        print("Tokyo is the capital of Japan")
    def lang(self):
        print("Japanese is the native language of Japan")
    def type(self):
        print("Japan is a developed country\n")
class USA:
    def capital(self):
        print("Washington D.C is the capital of USA")
    def lang(self):
        print("English is the native language of USA")
    def type(self):
        print("USA is a developed country\n")
class Spain:
    def capital(self):
        print("Madrid is the capital of Spain")
    def lang(self):
        print("Spanish is the native language of Spain")
    def type(self):
        print("Spain is a developed country\n")
j=Japan()
u=USA()
s=Spain()
for country in j,u,s:
    country.capital()
    country.lang()
    country.type()
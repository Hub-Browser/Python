from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("I can walk and run")
class dog(animal):
    def move(self):
        print("I can bark")
class snake(animal):
    def move(self):
        print("I can crawl")
class lion(animal):
    def move(self):
        print("I can roar")
h=human()
h.move()
d=dog()
d.move()
s=snake()
s.move()
l=lion()
l.move()
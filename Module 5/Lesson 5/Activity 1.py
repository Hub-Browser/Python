from abc import ABC, abstractmethod
class absclass(ABC):
    def print(self,x):
        print("Passed value:",x)
    @abstractmethod
    def task(self):
        print("We are inside an abstract method")

class test_class(absclass):
    def task(self):
        print("We are inside the subclass")

test_obj=test_class()
test_obj.task()
test_obj.print(1000)
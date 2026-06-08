class person:
    def __init__(self,name,id) -> None:
        self.name=name
        self.id=id
    def display(self):
        print(self.name)
        print(self.id)
class employee(person):
    def __init__(self, name, id, salary, post) -> None:
        self.salary=salary
        self.post=post
        person.__init__(self,name,id)
obj=employee("Aarush",2026,300000,"Manager")
obj.display()
print(obj.salary)
print(obj.post)
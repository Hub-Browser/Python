class vehicle:
    def __init__(self,name,maxspeed,mileage) -> None:
        self.name=name
        self.maxpseed=maxspeed
        self.mileage=mileage
class bus(vehicle):
    pass
school_bus=bus("School Volvo",180,12)
print(f"Name: {school_bus.name}\n Maximum speed: {school_bus.maxpseed}\n Mileage: {school_bus.mileage}")

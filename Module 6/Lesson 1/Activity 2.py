class vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
bmw=vehicle(240,18)
print(f"BMW can travel at a speed of {bmw.max_speed} and has a mileage of {bmw.mileage}.")
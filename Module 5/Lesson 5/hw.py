class BMW:
    def __init__(self,fuel_type,max_speed) -> None:
        self.fuel_type=fuel_type
        self.max_speed=max_speed
class Ferrari:
    def __init__(self,fuel_type,max_speed) -> None:
        self.fuel_type=fuel_type
        self.max_speed=max_speed
bmw=BMW("Petrol","80 km/h")
ferrari=Ferrari("Diesel","200 km/h")
for i in bmw,ferrari:
    print(f"Name: {i.__class__.__name__}\nFuel type: {i.fuel_type}\nMax speed: {i.max_speed}\n")
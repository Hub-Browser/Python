class vehicle:
    def __init__(self,seat_cap) -> None:
        self.seat_cap=seat_cap
    def fare(self):
        farep=self.seat_cap*100*1.1
        return farep
class bus(vehicle):
    pass

obj=bus(50)
print(obj.fare())
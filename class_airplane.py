
class Airplane:

    def __init__(self, marka, model, year, max_speed):
        self.marka = marka
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = False

    def take_off(self):
        self.is_flying = True
        message_take = f"{self.marka} {self.model} was take off."
        return message_take

    def fly(self, km):
        self.odometer += km
        message_fly = f"{self.marka} {self.odometer}km при полете {self.max_speed} km/h."
        return message_fly

    def land(self):
        self.is_flying = False
        message_land = f"{self.marka} приземлился, одометр {self.odometer}km."
        return message_land


start = Airplane("Истребитель", "Su-27", "", 3500)
print(start.take_off())
print(start.fly(600))
print(start.fly(600))
print(start.land())
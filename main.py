# HW 1
class Car:

    def __init__(self, title, model, weight, hp, nm, max_speed, color):
        self.title = title
        self.model = model
        self.weight = weight
        self.hp = hp
        self.nm = nm
        self.max_speed = max_speed
        self.color = color

    """CarTitle CarModel engine started!"""

    def start_engine(self):
        print(f"{self.title} {self.model} engine started!")

    """CarTitle CarModel engine stoped!"""

    def stop_engine(self):
        print(f"{self.title} {self.model} engine stoped!")

    """CarTitle CarModel All Info"""

    def info(self):
        print(f"Title: {self.title}, Model: {self.model}, Weight: {self.weight}, Hp: {self.hp}, Nm: {self.nm},"
              f"Max Speed: {self.max_speed}, Color: {self.color}")


bmv = Car("BMV", "x5-e53", 350, 100, 200, "350km/h", "BLACK")
bmv.start_engine()
bmv.stop_engine()
bmv.info()

mercedes = Car("Mercedes", "C-230", 100, 250, 200, "400m/h", "RED")
mercedes.start_engine()
mercedes.stop_engine()
mercedes.info()

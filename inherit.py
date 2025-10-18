class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def drive(self):
     return f"the man would drive{self.year}{self.make}{self.model}-car"
class tesla(car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size
    def drive(self):
        return f"the car mentioned is the tesla car with the battery size of {self.battery_size} kWh"
my_car = car("Toyota", "Camry", 2020)
print(my_car.drive())
my_car2=tesla("Tesla", "Model S", 2022, 100)
print(my_car2.drive())
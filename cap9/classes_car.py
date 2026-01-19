class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def read_odometer(self):
        print(f'esse carro tem {self.odometer_reading}km rodados.')

    def update_odometer(self, km):
        self.odometer_reading = km
        print(f'nova quilometragem do {self}: {km}')

    def increment_odometer(self, km):
        self.odometer_reading += km
        print(f'nova quilometragem incrementada do {self}: {km}')

class EletricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery = Battery()  
    
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('o carro tem: ',self.battery_size,'MiH')

carro1 = EletricCar('lamborghni', 'huracan', 2017)

carro1.battery.describe_battery() 
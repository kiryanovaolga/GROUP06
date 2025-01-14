# identifikacni_funkce.py

class Car:
    def __init__(self):
        self.name = 'Super car'
    
    def __eq__(self, other):
        return self.name == other.name

    def info(self):
        print('call info', self)

class SportCar(Car):
    pass


car = Car()
sport_car = SportCar()
x = car

print(car == sport_car)

print('id --------------')
print(id(car))
print(id(x))
print(id(sport_car))

print('type --------------')
print(type(car))
print(type(sport_car))
print(type(car) is Car)
print(type(sport_car) is Car)

print('isinstance --------------')
print(isinstance(sport_car, Car))
print(isinstance(sport_car, SportCar))
print(isinstance(sport_car, (SportCar, int)))

print('vars --------------')
print(vars(car)) # dict atributů a hodnot
print(dir(car)) # názvy atributů a metod
print(car.__class__.__name__)

print('getattr, hasattr, setattr, delattr')
setattr(car, 'power', 100)
print(hasattr(car, 'power'))

# tyto řádky dělají to stejné
x = getattr(car, 'info')
x()
car.info()

for name in dir(car):
    if not name.startswith('_'):
        setattr(car, name, None)

print(car.name)
print(car.power)
print(car.info)

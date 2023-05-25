class Race: 
  def __init__(self, race_name, car_limit, driver_limit):
    self.race_name = race_name
    self.car_limit = car_limit
    self.driver_limit = driver_limit

class Car:
  def __init__(self, name, max_speed):
    self.name = name
    self.max_speed = max_speed

  def start(self):
    print('Vroom!')

  def talk(self, driver):
    print(f'Hello, {driver}, I am {self.name}.')

race = Race("indy 500", [], 15)

myCar = Car('Kitt', 180)
myOtherCar = Car('Speedy', 55)

myCar.talk('Michael')
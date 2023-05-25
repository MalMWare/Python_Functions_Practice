class Race: 
  def __init__(self, race_name, car_limit, driver_limit):
    self.race_name = race_name
    self.car_limit = car_limit
    self.driver_limit = driver_limit

  def add_driver(self, driver):
    if len(self.car_limit) <= self.driver_limit:
      self.car_limit.append(driver)

  def get_average_ranking(self):
    sum = 0
    for d in self.car_limit:
      sum += d.driver_ranking
    return sum / len(self.car_limit)


class Driver:
  number_of_drivers = 0
  def __init__(self, driver_name, driver_age, driver_ranking):
    self.driver_name = driver_name
    self.driver_age = driver_age
    self.driver_ranking = driver_ranking
    Driver.number_of_drivers += 1

  def get_ranking(self):
    return self.driver_ranking

class Car:
  def __init__(self, name, max_speed):
    self.name = name
    self.max_speed = max_speed

  def start(self):
    print('Vroom!')

  def talk(self, driver):
    print(f'Hello, {driver}, I am {self.name}.')

my_driver = Driver('Lewis Hamilton', 28, 1)
print(my_driver.get_ranking())

d1 = Driver('Lewis Hamilton', 36, 83)
d2 = Driver('Eliud Kipchoge', 36, 95)
d3 = Driver('Sebastian Vettel', 34, 76)
d4 = Driver('Ayrton Senna', 34, 99)
race= Race("indy 500", [d1, d2, d3, d4], 15)

race.add_driver(d1)
race.add_driver(d2)
race.add_driver(d3)
race.add_driver(d4)

print(race.get_average_ranking())

# myCar = Car('Kitt', 180)
# myOtherCar = Car('Speedy', 55)

# myCar.talk('Mal')
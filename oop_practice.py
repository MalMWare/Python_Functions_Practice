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

# my_driver = Driver('Lewis Hamilton', 28, 1)
# print(my_driver.get_ranking())

# d1 = Driver('Lewis Hamilton', 36, 83)
# d2 = Driver('Eliud Kipchoge', 36, 95)
# d3 = Driver('Sebastian Vettel', 34, 76)
# d4 = Driver('Ayrton Senna', 34, 99)
# race= Race("indy 500", [d1, d2, d3, d4], 15)

# race.add_driver(d1)
# race.add_driver(d2)
# race.add_driver(d3)
# race.add_driver(d4)

# print(race.get_average_ranking())

# myCar = Car('Kitt', 180)
# myOtherCar = Car('Speedy', 55)

# myCar.talk('Mal')


class Person:
  def __init__(self,in_name,in_age):
    self.name = in_name
    self.age = in_age
      
  def get_name(self):
    return self.name

class Customer(Person):
  def __init__(self, name, age):
    super.__init__(name, age)
    self.has_ticket = false
    self.in_zoo = false

  def buy_ticket(self):
    if self.age >= 18:
      print(f'{self.name} has bought a ticket! Enjoy!')
    else:
      print(f'{self.name} has bought a child ticket! dont get to close to the lions.')

  def enter_zoo(self, zoo):
    if self.has_ticket == True:
      self.has_ticket = False
      zoo.add_customer(self.name)
      self.in_zoo = True
    else:
      print(f'{self.name} does not have a ticket. Please go buy one!')

  def exit_zoo(self, zoo):
    if self.in_zoo == True:
      self.in_zoo = False
      zoo.remove_customer(self.name)
    else:
      print(f'{self.name}...you can not leave a place you are not in')



class Zoo:
  def __init__(self,name="Local Zoo"):
    self.name = name
    self.animals = []
    self.customers = []

  def add_animal(self, animal):
    self.animals.append(animal)
    print(f"{self.name} has a(n) {animal}")
  
  def add_animals(self, animals):
    self.animals.extend(animals)
    print(f"{self.name} has many animals")
  
  def add_customer(self, name):
    self.customers.append(name)
    print(f"{name} has entered {self.name}")

  def remove_customer(self, name):
    self.customers.remove(name)
    print(f"{name} has left {self.name}")
  
  def visit_animals(self):
    for a in self.animals:
      print(f"visiting {a.get_name()}")
      a.make_noise()
      a.eat_food()

class Animal:
  def __init__(self,name):
    self.name = name
  def get_name(self):
    return self.name
  def make_noise(self):
    print("Every animal makes noise")
  def eat_food(self):
    print("All creatures need sustenance")

nycZoo = Zoo("NYC Zoo")

salmon = Fish("salmon")
robin = Bird("robin")
bonobo = Chimp("bonobo")
nycZoo.add_animals([salmon, robin, bonobo])

alice = Customer("Alice",25)
bob = Customer("Bob",20)
charlie = Customer("Charlie",10)
dave = Customer("Dave",30)
for c in [alice, bob, charlie, dave]:
  c.buy_ticket()
  c.enter_zoo(nycZoo)
nycZoo.visit_animals()
for c in [alice, bob, charlie, dave]:
  c.exit_zoo(nycZoo)
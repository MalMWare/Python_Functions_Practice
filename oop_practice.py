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
  def __init__(self, in_name, in_age):
    super().__init__(in_name, in_age)
    self.has_ticket = False
    self.in_zoo = False

  def buy_ticket(self):
    if self.age >= 18:
      print(f'{self.name} has bought a ticket! Enjoy!')
    else:
      print(f'{self.name} has bought a child ticket! dont get to close to the lions.')
    self.has_ticket = True

  def enter_zoo(self, zoo):
    if self.has_ticket == True:
      zoo.add_customer(self.name)
      self.has_ticket = False
      self.in_zoo = True
    else:
      print(f'{self.name} does not have a ticket. Please go buy one!')

  def exit_zoo(self, zoo):
    if self.in_zoo == True:
      self.in_zoo = False
      zoo.remove_customer(self.name)


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

class Fish(Animal):
  def __init__(self, name):
    super().__init__(name)

  def make_noise(self):
    print('*splash*')

  def eat_food(self):
    print('i am a cannibal')

class Bird(Animal):
  def __init__(self, name):
    super().__init__(name)

  def make_noise(self):
    print('Tweet Tweet')

  def eat_food(self):
    print('bugs and frogs man')

class Chimp(Animal):
  def __init__(self, name):
    super().__init__(name)

  def make_noise(self):
    print('oooouuuuooo ahhhahhh')

  def eat_food(self):
    print('everything a human can eat')

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


# Watto needs a new system for organizing his inventory of podracers. 
# Help him do this by implementing an Object Oriented solution according to the following criteria.

# First, he'll need a general Podracer class defined with max_speed, condition (perfect, trashed, repaired) and price attributes. 
class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price
# Define a repair() method that will update the condition of the podracer to "repaired".
  def repair(self):
    self.condition = "repaired"

# Define a new class, that inherits the Podracer class, but also contains a special method called boost that will multiply max_speed by 2.
class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)
  
  def boost(self):
    self.max_speed *= 2
  
# Define another class that inherits Podracer and call this one SebulbasPod. 

# This class should have a special method called flame_jet that will update the condition of another podracer to "thrashed".

class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super().__init__(max_speed, condition, price)

  def flame_jet(self, other):
    other.condition = "thrashed"

pod1 = Podracer(4, 'thrashed', 500000)
pod2 = AnakinsPod(2, 'perfect', 100000)
pod3 = SebulbasPod(3, 'perfect', 300000)

pod1.repair()
print(pod1.condition)

pod2.boost()
print(pod2.max_speed)

pod3.flame_jet(pod1)
print(pod1.condition)

'''
Make sure to answer the following prompts about your coding experience:

How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
There are four pillars in OOP and they are Inheritance, Polymorphism, Encapsulation and Abstraction. There is only one that isnt being used and that is Polymorphism. 
Inheritance is demonstrated because two sub-class inherits methods from the original class. Encapsulation is being used because classes keep the iformation together. Abstraction is used by placing methods inside of classes that can hold all of the information and be broken down into smaller parts later. 

Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
no because OOP is the best way to write the code for this problem

How in particular did Object Oriented Programming assist in the solving of this problem?
By classifying everything so I dont have to repeat the same lines of code over and over again 
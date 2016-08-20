

class Animal(object):
    pass

## Dog is-an animal
class Dog(Animal):
    def __init__(self, name):
        ##Dog has-a name
        self.name = name

## Cat is-an animal
class Cat(Animal):
    ##Cat has-a name
    def __init__(self, name):
        self.name = name

## Person is-a person
class Person(object):
    ## Person has-a name 
    self.name = name
    ## Person has-a per of something

## Employee is-a person
class Employee(Person):
    def __init__(self, name, salary):
    ## This magic function imports the name and define salaty of a person
    super(Employee, self).__init__(name)
    self.salary = salary

## Fish is-an object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## Mary has-a Cat as a pet whose name is Satan
mary.pet = satan

## frank is-a person and is-an Employee. His salary is 120,000
frank = Employee("Frank", 120000)

##frank has-a Pet named rover. 
frank.pet = rover

##flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()


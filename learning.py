# -*- coding: utf-8 -*-
""" Examples from Python Programming Illustrated """

from functools import reduce

# list comprehension
SIZES = ['S', 'M', 'L', 'XL']
PERSONS = ['Men', 'Women', 'Boy', 'Girl']
CP = [(a, b) for a in SIZES for b in PERSONS]
print(CP)


# map
NUMBERS = [1, 2, 3, 4, 5]
SQUARES = map(lambda x: x * x, NUMBERS)
print(list(SQUARES))

# filter
ODD = filter(lambda x: x % 2 == 1, NUMBERS)
print(list(ODD))

# reduce, imported from functools
S = reduce(lambda a, b: a + b, NUMBERS, 20)


# decorators - property & setter, static method, class method
class Employee:
    # class attribute, defined outside a method
    Count = 0
    
    def __init__(self, lvl = 5):
        Employee.Count += 1
        # instance attribute, inside a method
        self.Level = lvl
        self._department = ""
    
    @property
    def department(self):
        """ protected property """
        return self._department

    @department.setter
    def department(self, dept):
        self._department = dept
        
    @classmethod
    def print_class_name(cls):
        print(cls.__name__)

    # neither self, nor cls is passed as first argument 
    @staticmethod
    def get_count():
        return Employee.Count
    

EMP = Employee()
EMP.print_class_name()
EMP.department = "Purchasing"
print(EMP.department, EMP.Level, Employee.get_count())

# inheritance, constructor with default argument
class Manager(Employee):
    def __init__(self, lvl = 1):
        super().__init__()
        self.Level = lvl
        
    def change_dept(self, dept):
        self._department = dept
       

MGR = Manager(0)
MGR.print_class_name()
MGR.change_dept('*')
print(MGR.Level, Employee.get_count(), MGR.department)


# multiple inheritance
class Vehicle:
    def show_vehicle_details(self):
        print("I am vehicle class")

class Sedan:
    def show_sedan_details(self):
        print("I am sedan class")

class Car(Vehicle, Sedan):
    def show_car_details(self):
        print("I am car class")

CAR = Car()
CAR.show_car_details()
CAR.show_sedan_details()
CAR.show_vehicle_details()

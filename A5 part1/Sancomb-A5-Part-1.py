import re
# Griffin Sancomb
# # cm25251


q1 = "ABCD+++1234+EFGH++****"


result = re.sub('[^a-zA-Z1-9 *][+]*', '-', q1)
print(result) # prints ABCD-1234-EFGH-****
# ################################################################
# # Write a one-line list comprehension that outputs the following list:
#
# For the first 30 integers (int numbers between 1 and 30 inclusive):
# if the number is odd, square it
# if the number is even, double it
# Note: Your answer must be a one-line list comprehension. Other solutions will not get any points.


q2 = [item ** 2 if (item % 2 == 1) else (item + item) for item in range(1, 31)]

print(len(q2), 'numbers in q2 list')
print(q2)
# 30 numbers in q2 list
# [1, 4, 9, 8, 25, 12, 49, 16, 81, 20, 121, 24, 169, 28, 225, 32,
#  289, 36, 361, 40, 441, 44, 529, 48, 625, 52, 729, 56, 841, 60]

# Using lambda and filter() functions, write one line of code that can filter any string from
# the str_list that has less than 4 characters. See the desired output.
#
# Note: Your answer must be one line and must use lambda and filter(). Other solutions will
# not get any points.

str_list = ['UMBC', 'UMD', 'UMB', 'TU']

q3 = filter(lambda name: name if (len(name) >= 4) else "", str_list)

print(type(q3))
print(list(q3))

# <class 'filter'>
# ['UMBC']

#
# Create a Vehicle class with three instance attributes: make, model, year
#
# Add a method named isNew()that returns True if the year equals 2021; else returns False
#
# Vehicle class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def isNew(self):
        return True if self.year == 2021 else False

q4 = Vehicle('Honda', 'Accord', 2021)
print(type(q4))
print(q4.__dict__)
print(Vehicle.isNew(q4))

# <class '__main__.Vehicle'>
# {'make': 'Honda', 'model': 'Accord', 'year': 2021}
# True

# Create a class SUV that inherits from Vehicle class. SUV has two additional instance attributes:
# transmission and milage. You must use *args and **kwargs in the constructor method of SUV class
# otherwise your answer doesn't get any points.
# SUV class
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def isNew(self):
        return True if self.year == 2021 else False

class SUV(Vehicle):
    def __init__(self, *Vehicle, **kwargs,):
        self.transmission = kwargs.get('transmission', "transmission")
        self.milage = kwargs.get('milage',"milage")
        super().__init__(Vehicle[0], Vehicle[1], Vehicle[2])

    def __init__(self, transmission, mileage, *args, **kwargs):
            self.transmission = transmission
            self.mileage = mileage
            super().__init__(*args, **kwargs)

q5 = SUV('Automatic', 75000, 'Honda', 'CRV', 2020)
print(type(q5))
print(q5.__dict__)
print(SUV.isNew(q5))
#
# <class '__main__.SUV'>
# {'transmission': 'Automatic', 'milage': 75000, 'make': 'Honda', 'model': 'CRV', 'year': 2020}
# False

# from car import Car
from electric_car import ElectricCar as EC, Car as C

my_beetle = C('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = EC('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

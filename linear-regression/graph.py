import matplotlib.pyplot as pl
import numpy as np
from sys import argv
from main import calculate
from point import Point

# get number of values by user and generates random points
num_of_elem = int(argv[1])
random_values_x = np.random.random_sample((num_of_elem, ))
random_values_y = np.random.random_sample((num_of_elem, )) 

# convert the random values into Point classes
lista = []
for n in range(0, num_of_elem):
    new_point = Point(random_values_x[n], random_values_y[n])
    lista.append(new_point)

# calculate the linear function using the points
values = calculate(lista)
a = values[1]
b = values[0]

# insert the line into the graph
x = np.arange(0, 5)
y = a * x + b
pl.plot(x,y)

# insert the points into the graph
for point in lista:
    pl.plot(point.x, point.y, marker='o', color='r', markersize=3)
    
pl.show()

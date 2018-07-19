import numpy as np
import csv 
from matplotlib import pyplot as plt

x1 = []
y1 = []

with open('altitude.csv', 'r') as csvfile:
    plots = csv.reader(csvfile)
    for row in plots:
        x1.append(float(row[0]))
        y1.append(float(row[1]))

x2 = []
y2 = []

with open('altitudefil.csv', 'r') as csvfile:
    plots = csv.reader(csvfile)
    for row in plots:
        x2.append(float(row[0]))
        y2.append(float(row[1])) 

plt.figure()
plt.plot(x1,y1, label='Altitude without filter')
plt.plot(x2,y2, 'r', label='Altitude with gaussian filter')
plt.xlabel('Time')
plt.ylabel('Altitude')
plt.title('Altitude plot from ZED camera')
plt.legend()
plt.show()
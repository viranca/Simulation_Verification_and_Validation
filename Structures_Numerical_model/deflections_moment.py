import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame
from math import *
from scipy import integrate

momentxz = pd.read_csv("momentxz.csv")
momentxy = pd.read_csv("momentxy.csv")

y_1 = []
x_1 = []
for i in range(0,len(momentxz.index)):
    if i < len(momentxz.index) -1 :
        a = momentxz.values[i,1]
        b = momentxz.values[i+1,1]
        c = momentxz.values[i,0]
        d = momentxz.values[i+1,0]

        fy = [a,b]
        fx = [c,d]
        dx = (c+d)/2
        first_int = integrate.simps(fy)
        y_1.append(first_int)
        x_1.append(dx)

y_deflections = []
x_coordinates = []

#1349
y_1[1349] = 0

for i in range(0,len(y_1)):
    if i < len(y_1) -1 :
        a = y_1[i]
        b = y_1[i+1]
        c = x_1[i]
        d = x_1[i+1]

        fy = [a,b]
        fx = [c,d]
        dx = (c+d)/2
        first_int = integrate.trapz(fy)

        y_deflections.append(first_int)

        x_coordinates.append(dx)

y_deflections = np.divide(y_deflections,(73100000000*1.1374E-05))
#newList = [y_deflections / (73100000000*1.1374E-05) for x in y_deflections]


plt.figure()
plt.plot(x_coordinates,y_deflections)

plt.figure()
plt.plot(momentxz.values[:,0], momentxz.values[:,1])

plt.show()
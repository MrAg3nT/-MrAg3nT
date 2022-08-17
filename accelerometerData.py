from engi1020.arduino.api import *
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime 
import time

t= 0
plt.axis([0, 1000, 0, 1])

for i in range(1000):
    t+=1
    X = (three_axis_get_accelX())
    Y = three_axis_get_accelY()
    Z = three_axis_get_accelZ()
    plt.xlabel("t / [s]")
    plt.ylabel("a / g")
    plt.plot(t, X, 'xb-', label='AccelX', linewidth=2)
    plt.plot(t, Y, 'r+', label='AccelY')
    plt.plot(t, Z, 'bo', label = 'AccelZ')
    plt.pause(0.05)
    
#plt.show()

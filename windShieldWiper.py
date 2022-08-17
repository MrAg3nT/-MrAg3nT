from engi1020.arduino.api import *
from time import sleep


#winsdshield wiper with servo meter
def mapp(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min


while True:
    val = analog_read(0)
    val = mapp(val, 0, 1023, 0, 180)
    servo_set_angle(7, val)
    sleep(0.0001)
    
while True:
    for angle in range(0, 120):
        servo_set_angle(7, angle)                 
        sleep(0.000001);                       
             
    for angle in range(120, 0, -1):
        angle -= 5
        servo_set_angle(7, angle)
        sleep(0.000001)
        
        
    #break
            


#print(wipers)

    

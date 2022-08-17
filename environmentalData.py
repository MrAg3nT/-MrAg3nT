from engi1020.arduino.api import *
from time import sleep

#environmental sensors
def environmentalData(threshold1, threshold2):
    
    """

    threshold1 = temperature in degree celcius
    threshold2 = pressure in pascal

    """
    oled_print(pressure_get_temp)
    print(f"Temperature is {pressure_get_temp()}")
    oled_print(pressure_get_pressure)
    print(f"Pressure is {pressure_get_pressure()}")
    oled_print(analog_read(6))
    print(f"Light level is {analog_read(6)}")
    
    #threshold check
    while True:
        
        if pressure_get_temp() > threshold1 or pressure_get_pressure() > threshold2:
            
            digital_write(4, True)
            buzzer_note(5, 800, 1)
            buzzer_note(5, 1020,1)
            buzzer_note(5, 400, 1)
            buzzer_note(5, 650, 1)
            
            print(f"Temperature is {pressure_get_temp()}")
            print(f"Pressure is {pressure_get_altitude}")
            
            sleep(1)
            
            if digital_read(6) == True:
                break
            
            
        else:  
            oled_print(pressure_get_temp)
            print(f"Temperature is {pressure_get_temp()}")
            oled_print(pressure_get_pressure)
            print(f"Pressure is {pressure_get_pressure()}")
            oled_print(analog_read(6))
            print(f"Pressure is {analog_read(6)}")

            
#print(environmentalData(20, 1000))


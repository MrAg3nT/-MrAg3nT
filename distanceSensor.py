from engi1020.arduino.api import *
from time import *
from inspect import getmembers, isfunction



while True:
    distance = ultra_get_centimeters(6)
    if distance < 0:
        digital_write(4, True)
        buzzer_note(5, 800, 1)
        buzzer_note(5, 1020,1)
        buzzer_note(5, 650, 1)
        
        if digital_read(6) == True:
            digital_write(4, False)
            break
        else:
            print(f"HIT BRAKE!!! ≈Distance is {distance} cm!")
            #oled_print(f"HIT BRAKE {distance} cm!")
    else:
        print(f"Distance is {distance} cm!")
        oled_print("HIT BRAKE!")
            
        sleep(1)
    
print(f"Current Distance gap is {distance} cm!")       

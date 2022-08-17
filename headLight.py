from engi1020.arduino.api import *
from time import sleep
from datetime import datetime

def milli():
    dt = datetime.now()
    return dt.microsecond

print(milli())


#headlight turn on/off

ledState = False
debouncedDuration = 50
lastButtonState = digital_read(6)
lastTimeButtonStatusChanged = milli()

while True:
    if milli() - lastTimeButtonStatusChanged >= debouncedDuration:
        buttonState = digital_read(6)
        if buttonState != lastButtonState:
            lastTimeButtonStatusChanged = milli()
            lastButtonState = buttonState
            if buttonState == False:
                if ledState == True:
                    ledState = False
                else:
                    ledState = True
            digital_write(4, ledState)
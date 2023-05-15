from RPi_GPIO_i2c_LCD import lcd
from time import sleep, strftime

## Callback function that will run on every display loop
def MyFunction(self):
    ## Show current time on line 2
    self.lcd.display_string(str(strftime("%d/%m %H:%M:%S").center(20,' ')),2)

## Initalize display with callback
lcdDisplay = lcd.HD44780(0x27,MyFunction)

## Set string value to buffer
lcdDisplay.set("The time is:",1)
sleep(6)
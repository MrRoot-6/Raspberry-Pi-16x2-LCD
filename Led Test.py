import time
from gpiozero import LED
from RPLCD.gpio import CharLCD
from RPi import GPIO


def lcddisplay(DISPLAY, TIME, lcd):
    lcd.cursor_pos = (0,0)
    lcd.clear()
    lcd.write_string(DISPLAY)
    if TIME != 0:
        time.sleep(TIME)
        lcd.clear()
    return True


lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=13, pin_rw=15, pin_e=16, pins_data=[21,22,23,24], charmap='A02', auto_linebreaks=True)

led = LED(21)
ACTIVE = True
i = 0

try:
    while ACTIVE:
        led.on()
        i += 1;
        time.sleep(0.05)
        led.off()
        lcddisplay("Times: %d"%i,0, lcd)
        time.sleep(0.05)
except KeyboardInterrupt:
    ACTIVE = False

del lcd
GPIO.cleanup()

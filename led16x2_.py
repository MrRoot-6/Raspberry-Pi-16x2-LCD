from RPLCD.gpio import CharLCD
from RPi import GPIO
import sys
import getopt
import time


global DISPLAY
global TIME
global PIN_RS
global PIN_RW
global PIN_E
global DATA_PINS
global ADDITIONAL_SYMBOL

# DISPLAY specify string to displayt on LED
# TIME specify time of displaing. Set 0 to leave displayed
# PINS specify connected pins rs,rw,ee,d0,d1,d2,d3,d4,d5,d6,d7 WARNING USE GPIO.BOARD PIN NUMBERS


if not len(sys.argv[1:]):
    sys.exit(0)
try:
    opts, args = getopt.getopt(sys.argv[1:], "p:d:t:",  ["pins", "display", "time"])
except getopt.GetoptError as err:
    print(err)
    sys.exit(0)


for o, a in opts:
    if o in ("-t", "--time"):
        TIME = float(a)
    elif o in ("-d", '--display'):
        DISPLAY = (str(a))
    elif o in ("-p", "--pins"):
        PINS = a.split(',')
    else:
        assert False, "Unsupported option!!!"

PIN_RS = int(PINS[0])
PIN_RW = int(PINS[1])
PIN_E = int(PINS[2])
DATA_PINS = PINS[3:]
for i in range(len(DATA_PINS)):
    DATA_PINS[i] = int(DATA_PINS[i])

lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=PIN_RS, pin_rw=PIN_RW, pin_e=PIN_E, pins_data=DATA_PINS, charmap='A02', auto_linebreaks=True)


def lcddisplay(DISPLAY, TIME, lcd):
    lcd.cursor_pos = (0,0)
    lcd.clear()
    lcd.write_string(DISPLAY)
    if TIME != 0:
        time.sleep(TIME)
        lcd.clear()
    return True

lcddisplay(DISPLAY, TIME, lcd)
del lcd
# Test how many times you can blink red LED before it crashes
## Connecting LCD to Raspberry Pi 3b+
| *Connect to*        | *LCD pin*           |
| ------------- |:-------------:|
| RPi 2 (5v) | 1 (VSS) |
| RPi 6 (GND) | 2 (VDD) |
| Center pin of potentiometr. ground to get max contrast| 3 (V0 - contrast pin) |
| RPi 13 (Register Select) | 4 (RS)|
| RPi 15 (Read/Write) | 5 (RW)|
| RPi 16 (Enable) | 6 (E) |
| ---- | 7 (Data pin 0) |
| ---- | 8 (Data pin 1) |
| ---- | 9 (Data pin 2) |
| ---- | 10 (Data pin 3) |
| RPi 21 | 11 (Data pin 4) |
| RPi 22 | 12 (Data pin 5) |
| RPi 23 | 13 (Data pin 6) |
| RPi 24 | 14 (Data pin 7) |
| Positive LED | 15 (A) |
| Negative LED| 16 (k) |

*You can change right pin with left when connecting potentiometr*

|Potentiometr||
| ------------- |:-------------:|
| Left | Ground |
| Center | LCD 3rd pin (V0 - contrast)|
| Right | 5v |

**We'll display number of times our led blinked on LCD 16x2**

**Now all we have to do is wire things up and test our diode**

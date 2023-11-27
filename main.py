from picozero import Speaker
from machine import Pin
import utime

trigger = Pin(3, Pin.OUT)
echo = Pin(4, Pin.IN)
speaker = Speaker (2)

def c_note():
    speaker.play('c4', 1)

def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   print("La distancia al objeto es ",distance,"cm")
   if distance < 15:
        speaker.play('c4', 0.5)


   
while True:
   ultra()
   utime.sleep(1)
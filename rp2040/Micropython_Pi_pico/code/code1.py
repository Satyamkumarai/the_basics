from machine import Pin 
from time import sleep
led = Pin(25,Pin.OUT)
for i in range(10):
    led.toggle()
    sleep(1)
import time
from pyA20.gpio import gpio
from pyA20.gpio import port

led = port.PA14
buttonRight = port.PA16
buttonLeft = port.PA18 

gpio.init()
gpio.setcfg(led,gpio.OUTPUT)
gpio.setcfg(buttonRight,gpio.INPUT)
gpio.setcfg(buttonLeft,gpio.INPUT)
gpio.pullup(buttonRight,gpio.PULLUP)
gpio.pullup(buttonLeft,gpio.PULLUP)

try:
    if (gpio.input(buttonLeft)==0):
        gpio.output(led,1)
    else:
        gpio.output(led,0)

except:
    print("unknown error")

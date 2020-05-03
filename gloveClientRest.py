import requests as req
import time
from pyA20.gpio import gpio
from pyA20.gpio import port

led = port.PA14
buttonRight = port.PA11
buttonLeft = port.PA12

gpio.init()
gpio.setcfg(led,gpio.OUTPUT)
gpio.setcfg(buttonRight,gpio.INPUT)
gpio.setcfg(buttonLeft,gpio.INPUT)
gpio.pullup(buttonRight,gpio.PULLUP)
gpio.pullup(buttonLeft,gpio.PULLUP)

url = input("Server ip-ny yazyn: ")

while True:
	try:
		if(gpio.input(buttonLeft)==0):
			gpio.output(led,1)
			resp = req.get("http://"+url+":5000/state/2")
			print(resp.text)
			gpio.output(led,0)
		elif(gpio.input(buttonRight)==0):
			gpio.output(led,1)
			resp = req.get("http://"+url+":5000/state/1")
			print(resp.text)
			gpio.output(led,0)
	except:
		print("unknown error")

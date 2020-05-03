import requests as req
import pyautogui

while True:
	resp = req.get("http://localhost:5000/state")
	print(resp.text)
	if (resp.text=="switch:1"):
		pyautogui.press('right')
		resp = req.get("http://localhost:5000/state/0")
		print(resp.text)
	if (resp.text=="switch:2"):
		pyautogui.press('left')
		resp = req.get("http://localhost:5000/state/0")
		print(resp.text)
import translators as ts
import pyautogui
import time
import pyperclip
import pickle
import re

print(pyautogui.pixelMatchesColor(1469, 165, (120, 200, 0), tolerance=20))	
print(pyautogui.pixelMatchesColor(1018, 335, (120, 200, 0), tolerance=20))
if (pyautogui.pixelMatchesColor(813, 395, (88, 204, 2), tolerance=10)):
			print("start")
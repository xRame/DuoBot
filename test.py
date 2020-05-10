import translators as ts
import pyautogui
import time
import pyperclip
import pickle
import re

choose2 = {}

with open('choose2.txt', encoding='UTF-8') as inp:
	for i in inp.readlines():
		key,val = i.strip().split(':')
		choose2[key] = val

pyautogui.moveTo(561, 392)
pyautogui.dragTo(1309, 393, duration=0.5)  # drag mouse to XY
time.sleep(0.2)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.2)
text = pyperclip.paste()
text = ts.google(text, 'ru', 'en')
text = re.sub('\n.',"", text)
text = re.sub('\r',"", text)
pyautogui.moveTo(1287, 724)
pyautogui.dragTo(532, 461, duration=0.5)  
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'c')
time.sleep(0.2)
asnwers = (str)(pyperclip.paste())
result2 = re.sub('\d',"", asnwers)
result2 = re.sub('\r',"", result2)
result3 = result2.split('\n')
while("" in result3):
	result3.remove("")
#print(result3)
try:
	if (choose2[text] != 'None'): # если есть в списке
		print("i know")
		answ = choose2[text]
		if(result3[0] == answ):
			pyautogui.click(829, 586)
		elif(result3[1] == answ):	
			pyautogui.click(1142, 581)
		elif(result3[2] == answ):	
			pyautogui.click(837, 662)
		else:
			pyautogui.click(1102, 660)
		pyautogui.click(1362, 972)
		#print("check")
		check()	

except KeyError:							# если есть нет в списке
		print("i don't know")
		pyautogui.click(829, 586)
		pyautogui.click(1362, 972)
		time.sleep(.2)

		print(pyautogui.pixelMatchesColor(569, 900, (255, 255, 255), tolerance=2))
		print(pyautogui.pixelMatchesColor(592, 875, (255, 255, 255), tolerance=2))
		if (pyautogui.pixelMatchesColor(1782, 971, (255, 193, 193), tolerance=2)): # проверка на ошибки 
			if (pyautogui.pixelMatchesColor(569, 900, (255, 255, 255), tolerance=2)):
				pyautogui.moveTo(606, 902)
				pyautogui.dragTo(955, 903, duration=0.5)  # drag mouse to XY
				pyautogui.hotkey('ctrl', 'c')
				time.sleep(0.2)
				choose2[text] = (str)(pyperclip.paste())
				#print(choose2)
				with open('choose2.txt','w', encoding='UTF-8') as out:
					for key,val in choose2.items():
						out.write('{}:{}\n'.format(key,val))
			elif (pyautogui.pixelMatchesColor(592, 875, (255, 255, 255), tolerance=2)):
				pyautogui.moveTo(608, 874)
				pyautogui.dragTo(1074, 878, duration=0.5)  # drag mouse to XY
				pyautogui.hotkey('ctrl', 'c')
				time.sleep(0.2)
				choose2[text] = (str)(pyperclip.paste())
				#print(choose2)
				with open('choose2.txt','w', encoding='UTF-8') as out:
					for key,val in choose2.items():
						out.write('{}:{}\n'.format(key,val))			
			pyautogui.click(1356, 928)			
		else:
			choose2[text] = result3[0]
			with open('choose2.txt','w', encoding='UTF-8') as out:
				for key,val in choose2.items():
					out.write('{}:{}\n'.format(key,val))
			pyautogui.click(1356, 928)					

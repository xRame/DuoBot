import translators as ts
import pyautogui
import time
import pyperclip
import re
import os

en_ru = {}
ru_en = {}
choose3 = {}
choose2 = {}

with open('en_ru.txt', encoding='UTF-8') as inp:
	for i in inp.readlines():
		key,val = i.strip().split(':')
		en_ru[key] = val
with open('ru_en.txt', encoding='UTF-8') as inp:
	for i in inp.readlines():
		key,val = i.strip().split(':')
		ru_en[key] = val
with open('choose3.txt', encoding='UTF-8') as inp:
	for i in inp.readlines():
		key,val = i.strip().split(':')
		choose3[key] = val
with open('choose2.txt', encoding='UTF-8') as inp:
	for i in inp.readlines():
		key,val = i.strip().split(':')
		choose2[key] = val


def start():
	go = True
	while True:
		# if (pyautogui.pixelMatchesColor(813, 395, (88, 204, 2), tolerance=10)):
		# 	print("start")
		# 	go = True
		# 	pyautogui.click(1255, 969)
		# else:
		# 	go = False	
		while go == True:
			quest = get_quest()
			#print(quest)
			if (pyautogui.pixelMatchesColor(165, 955, (184, 242, 139), tolerance=2)):
				pyautogui.click(1358, 967)
			elif (pyautogui.pixelMatchesColor(1020, 986, (24, 153, 214), tolerance=20)): #next lesson
				pyautogui.click(1020, 986)	
			elif pyautogui.pixelMatchesColor(1471, 160, (120, 200, 0), tolerance=20):	
				print("Finish")
				go = False
			elif (pyautogui.pixelMatchesColor(1018, 335, (120, 200, 0), tolerance=10)): #end of a lesson
				print("Finish")
				go = False	
			elif pyautogui.pixelMatchesColor(890, 360, (28, 176, 246), tolerance=2):
				skip_audio()
			elif pyautogui.pixelMatchesColor(934, 433, (28, 176, 246), tolerance=2):	
				skip_audio2()
			
			elif(quest == 'Повторите это предложение вслух'):
				pyautogui.click(665, 972)
			elif(quest =='Отметьте правильное значение'):
				choose_3()
			elif(quest =='Заполните пропуск'):
				fill()	
			elif (quest == 'Введите перевод на английский'):
				translate_to_en()
			elif (quest == 'Введите перевод на русский'):
				translate_to_ru()	
			elif re.search(r'\bНапишите\b', quest):
				write_smth(quest)
			elif re.search(r'Отметьте \b', quest):	
				choose(quest)
			else:
				break	
		return



def choose_theme():
	print()


def skip_audio():
	pyautogui.click(499, 936)
	time.sleep(.5)
	check()

def skip_audio2():
	pyautogui.click(615, 970)
	time.sleep(.5)
	check()

def fill():
	pyautogui.moveTo(661, 392)
	pyautogui.dragTo(1309, 393, duration=0.3)  # drag mouse to XY
	time.sleep(0.2)
	pyautogui.hotkey('ctrl', 'c')
	time.sleep(0.2)
	text = pyperclip.paste()
	text = ts.google(text, 'ru', 'en')
	text = re.sub('\n.',"", text)
	text = re.sub('\r',"", text)
	pyautogui.moveTo(1287, 724)
	pyautogui.dragTo(632, 461, duration=0.3)  
	time.sleep(0.5)
	pyautogui.hotkey('ctrl', 'c')
	time.sleep(0.2)
	asnwers = (str)(pyperclip.paste())
	result2 = re.sub('\d',"", asnwers)
	result2 = re.sub('\r',"", result2)
	result3 = result2.split('\n')
	while("" in result3):
		result3.remove("")
	print(result3)
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
			print("check")
			check()	

	except KeyError:							# если есть нет в списке
			print("i don't know")
			pyautogui.click(829, 586)
			pyautogui.click(1362, 972)

			if (pyautogui.pixelMatchesColor(1782, 971, (255, 193, 193), tolerance=2)): # проверка на ошибки 
				if (pyautogui.pixelMatchesColor(594, 901, (255, 255, 255), tolerance=2)):
					pyautogui.moveTo(606, 902)
					pyautogui.dragTo(955, 903, duration=0.5)  # drag mouse to XY
					pyautogui.hotkey('ctrl', 'c')
					time.sleep(0.2)
					choose2[text] = (str)(pyperclip.paste())
					print(choose2)
					with open('choose2.txt','w', encoding='UTF-8') as out:
						for key,val in choose2.items():
							out.write('{}:{}\n'.format(key,val))
				elif (pyautogui.pixelMatchesColor(592, 875, (255, 255, 255), tolerance=2)):
					pyautogui.moveTo(608, 874)
					pyautogui.dragTo(1074, 878, duration=0.5)  # drag mouse to XY
					pyautogui.hotkey('ctrl', 'c')
					time.sleep(0.2)
					choose2[text] = (str)(pyperclip.paste())
					print(choose2)
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


def choose(arr):
	r1 = re.sub('Отметьте слово ',"", arr)
	r2 = re.sub(r"[«»]","", r1)		#choose a word
	r2 = ts.google(r2, 'ru', 'en').lower()
	print(r2)

	pyautogui.moveTo(1319, 677)
	pyautogui.dragTo(703, 617, duration=0.3)  # drag mouse to XY
	time.sleep(0.5)
	pyautogui.hotkey('ctrl', 'c')
	time.sleep(0.2)
	text = (str)(pyperclip.paste())
	result2 = re.sub('\d'," ", text)
	result3 = result2.split()

	if(result3[0] == r2):
		pyautogui.click(771, 563)
	elif(result3[1] == r2):
		pyautogui.click(970, 589)
	else:
		pyautogui.click(1146, 576)

	#time.sleep(0.2)
	pyautogui.click(1362, 972)	
	check()

def choose_3():
	pyautogui.moveTo(661, 392)
	pyautogui.dragTo(1309, 393, duration=0.5)  # drag mouse to XY
	pyautogui.hotkey('ctrl', 'c')
	time.sleep(0.2)
	text = pyperclip.paste()
	text1 = text
	text = ts.google(text, 'ru', 'en')
	#print(text)
	pyautogui.moveTo(1287, 724)
	pyautogui.dragTo(627, 470, duration=0.5)  # drag mouse to XY
	pyautogui.hotkey('ctrl', 'c')
	time.sleep(0.2)
	asnwerts = (str)(pyperclip.paste())
	result2 = re.sub('\d',"", asnwerts)
	result2 = re.sub('\r',"", result2)
	result3 = result2.split('\n')
	while("" in result3):
		result3.remove("")
	print(result3)
	try:
		answ = choose3[text1]
		print(answ)
		if(result3[0] == answ):
			pyautogui.click(839, 531)
		elif(result3[1] == answ):
			pyautogui.click(849, 599)
		else:
				pyautogui.click(870, 668)
	except KeyError:		
		if(result3[0] == text):
			pyautogui.click(839, 531)
		elif(result3[1] == text):
			pyautogui.click(849, 599)
		else:
			pyautogui.click(870, 668)

	pyautogui.click(1362, 972)

	if (pyautogui.pixelMatchesColor(165, 955, (255, 193, 193), tolerance=2)):
		pyautogui.moveTo(609, 954)
		pyautogui.dragTo(1156, 971, duration=0.3)  # drag mouse to XY
		time.sleep(0.5)
		pyautogui.hotkey('ctrl', 'c')
		time.sleep(0.2)
		choose3[text1] = (str)(pyperclip.paste())
		#print(choose3)
		with open('choose3.txt','w', encoding='UTF-8') as out:
			for key,val in choose3.items():
				out.write('{}:{}\n'.format(key,val))




	check()

def write_smth(arr):
	r1 = re.sub('Напишите',"", arr)
	r1 = re.sub(' на английском',"", r1)
	r2 = re.sub(r'[""]',"", r1)		#choose a word
	r2 = ts.google(r2, 'ru', 'en').lower()
	pyautogui.click(928, 566)
	pyperclip.copy(r2)
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.click(1362, 972)	
	check()

def get_quest():
	pyautogui.moveTo(468, 335)
	pyautogui.dragTo(1445, 335, duration=0.3)  # drag mouse to XY
	time.sleep(0.5)
	pyautogui.hotkey('ctrl', 'c')
	time.sleep(0.2)
	text = (str)(pyperclip.paste())
	return text

def get_text():
	pyautogui.moveTo(675, 394)
	pyautogui.dragTo(1400, 412, duration=0.3)  # drag mouse to XY
	time.sleep(0.5)
	pyautogui.hotkey('ctrl', 'c')
	time.sleep(0.2)
	text = (str)(pyperclip.paste())
	return text

def translate_to_en():
	text = get_text()
	answ = ts.google(text, 'ru', 'en')
	try:
		if ru_en[text] == 'None':
			answ = ts.google(text, 'ru', 'en')
			ru_en[text]=answ
		else:
			answ = ru_en[text]
	except KeyError:
		pass

	pyautogui.click(685, 672)
	pyperclip.copy(answ)
	pyautogui.hotkey('ctrl', 'v')

	pyautogui.click(1362, 972)	
	if (pyautogui.pixelMatchesColor(165, 955, (255, 193, 193), tolerance=2)):
		pyautogui.moveTo(609, 954)
		pyautogui.dragTo(1156, 971, duration=0.3)  # drag mouse to XY
		time.sleep(0.5)
		pyautogui.hotkey('ctrl', 'c')
		time.sleep(0.2)
		ru_en[text] = (str)(pyperclip.paste())
		with open('ru_en.txt','w', encoding='UTF-8') as out:
			for key,val in ru_en.items():
				out.write('{}:{}\n'.format(key,val))

	
	check()

def translate_to_ru():
	text = get_text()
	answ = ts.google(text, 'en', 'ru')
	try:
		if en_ru[text] == 'None':
			answ = ts.google(text, 'en', 'ru')
			en_ru[text]=answ
		else:
			answ = en_ru[text]
	except KeyError:
		pass

	pyautogui.click(685, 672)
	pyperclip.copy(answ)
	pyautogui.hotkey('ctrl', 'v')

	pyautogui.click(1362, 972)	
	if (pyautogui.pixelMatchesColor(165, 955, (255, 193, 193), tolerance=2)):
		pyautogui.moveTo(609, 954)
		pyautogui.dragTo(1156, 971, duration=0.3)  # drag mouse to XY
		time.sleep(0.5)
		pyautogui.hotkey('ctrl', 'c')
		time.sleep(0.2)
		en_ru[text] = (str)(pyperclip.paste())
		with open('en_ru.txt','w', encoding='UTF-8') as out:
			for key,val in en_ru.items():
				out.write('{}:{}\n'.format(key,val))
	
	check()

def check():
	if (pyautogui.pixelMatchesColor(165, 955, (184, 242, 139), tolerance=2)):
		pyautogui.click(1358, 967)
	if (pyautogui.pixelMatchesColor(165, 955, (255, 193, 193), tolerance=2)):
		pyautogui.click(1358, 967)	

start()
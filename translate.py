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
write = {}
print("DuoBot was started")

class File_Magager:
	def load(list,name_list):
		try:
			with open(name_list + '.txt', encoding='UTF-8') as inp:
				for i in inp.readlines():
					key,val = i.strip().split(':')
					list[key] = val
			print("\t" + name_list + ' was loaded successfully!')		
		except ValueError:
			print("\t" + "there are some shit in file: " + name_list)
	
	def write(list,name_list):
		with open('name_list.txt','w', encoding='UTF-8') as out:
				for key,val in list.items():
					out.write('{}:{}\n'.format(key,val))	
 
class Quester:
	def get_quest():
			pyautogui.moveTo(468, 335)
			pyautogui.dragTo(1445, 335, duration=0.3)  # drag mouse to XY
			time.sleep(0.5)
			pyautogui.hotkey('ctrl', 'c')
			time.sleep(0.2)
			quest = (str)(pyperclip.paste())
			return quest

	def get_text():
		pyautogui.moveTo(575, 394)
		pyautogui.dragTo(1400, 412, duration=0.3)  # drag mouse to XY
		time.sleep(0.5)
		pyautogui.hotkey('ctrl', 'c')
		time.sleep(0.2)
		text = (str)(pyperclip.paste())
		return text		

class Distributor:
	def next_lesson():
		if (pyautogui.pixelMatchesColor(873, 982, (28, 176, 246), tolerance=20)): #next training
			pyautogui.click(1237, 973)
			time.sleep(3)	
		elif (pyautogui.pixelMatchesColor(1219, 987, (28, 176, 246), tolerance=20)): #train again
			pyautogui.click(1219, 987)
			time.sleep(3)
		elif (pyautogui.pixelMatchesColor(449, 977, (28, 176, 246), tolerance=20)):	#train 
			pyautogui.click(438, 977)
			time.sleep(3)	
		Checker.check() 

	def next_qustion():
		quest = Quester.get_quest()
		if pyautogui.pixelMatchesColor(890, 360, (28, 176, 246), tolerance=2):
			Skipper.skip_audio()
		elif pyautogui.pixelMatchesColor(934, 433, (28, 176, 246), tolerance=2):	
			Skipper.skip_audio2()
		elif(quest == 'Повторите это предложение вслух'):
			pyautogui.click(665, 972)
		elif(quest =='Отметьте правильное значение'):
			Chooser.choose_3()
		elif(quest =='Заполните пропуск'):
			Filler.fill()	
		elif (quest == 'Введите перевод на английский'):
			Translator.translate_to_en()
		elif (quest == 'Введите перевод на русский'):
			Translator.translate_to_ru()	
		elif re.search(r'\bНапишите\b', quest):
			Translator.write_smth(quest)
		elif re.search(r'Отметьте \b', quest):	
			Chooser.choose(quest)
		else:
			print("Waiting")	

class Checker:
	def check():
		pyautogui.click(1362, 972)
		time.sleep(1)
		if (pyautogui.pixelMatchesColor(165, 955, (184, 242, 139), tolerance=2)): 	# true
			#pyautogui.click(1358, 967)
			return True
		if (pyautogui.pixelMatchesColor(165, 955, (255, 193, 193), tolerance=2)): 	# false
			#pyautogui.click(1358, 967)	
			return False

class Skipper:
	def skip_audio():
		print("skip audio")
		pyautogui.click(499, 936)
		time.sleep(.5)
		Checker.check()

	def skip_audio2():
		print("skip audio2")
		pyautogui.click(615, 970)
		time.sleep(.5)
		Checker.check()

class Chooser:
	def choose(arr):
		print("start choose")
		r1 = re.sub('Отметьте слово ',"", arr)
		r2 = re.sub(r"[«»]","", r1)		#choose a word
		r2 = ts.google(r2, 'ru', 'en').lower()

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

		if Checker.check():
			pyautogui.click(1358, 967)
		else:
			pyautogui.click(1358, 967)		

	def choose_3():
		print("start choosing from 3")
		pyautogui.moveTo(561, 392)
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
		#print(result3)
		try:
			answ = choose3[text1]
			print("\tI know the answer on" + str(text1) + ' is: ' + str(answ))
			if(result3[0] == answ):
				pyautogui.click(839, 531)
			elif(result3[1] == answ):
				pyautogui.click(849, 599)
			else:
				pyautogui.click(870, 668)
		except KeyError:
			print("\ti trying by myslef")		
			if(result3[0] == text):
				pyautogui.click(839, 531)
			elif(result3[1] == text):
				pyautogui.click(849, 599)
			else:
				pyautogui.click(870, 668)

		if not Checker.check():
			pyautogui.moveTo(582, 954)
			pyautogui.dragTo(1156, 971, duration=0.3)  # drag mouse to XY
			time.sleep(0.5)
			pyautogui.hotkey('ctrl', 'c')
			time.sleep(0.2)
			choose3[text1] = (str)(pyperclip.paste())
			print("\tI don't know the answer,but at the next time i will answer: " + str(choose3[text1]))
			File_Magager.write(choose3,'choose3')
			pyautogui.click(1358, 967)
		else:	
			pyautogui.click(1358, 967)

class Translator:
	def translate_to_en():
		print("start translate_to_en")
		text = Quester.get_text()
		answ = ts.google(text, 'ru', 'en')
		try:
			if ru_en[text] == 'None':
				answ = ts.google(text, 'ru', 'en')
				ru_en[text]=answ
			else:
				answ = ru_en[text]
				print("\tI know the answer on" + str(text) + ' is: ' + str(answ))
		except KeyError:
			pass

		pyautogui.click(685, 672)
		pyperclip.copy(answ)
		pyautogui.hotkey('ctrl', 'v')

		
		if not Checker.check():
			pyautogui.moveTo(576, 955)
			pyautogui.dragTo(1156, 971, duration=0.5)  # drag mouse to XY
			time.sleep(0.5)
			pyautogui.hotkey('ctrl', 'c')
			time.sleep(0.2)
			ru_en[text] = (str)(pyperclip.paste())
			print("\tI don't know the answer,but at the next time i will answer: " + str(ru_en[text]))
			File_Magager.write(ru_en,'ru_en')
			pyautogui.click(1358, 967)
		else:
			pyautogui.click(1358, 967)			


	def translate_to_ru():
		print("start translate_to_ru")
		text = Quester.get_text()
		answ = ts.google(text, 'en', 'ru')
		try:
			if en_ru[text] == 'None':
				answ = ts.google(text, 'en', 'ru')
				en_ru[text]=answ
			else:
				answ = en_ru[text]
				print("\tI know the answer on" + str(text) + ' is: ' + str(answ))
		except KeyError:
			pass

		pyautogui.click(685, 672)
		pyperclip.copy(answ)
		pyautogui.hotkey('ctrl', 'v')

		if not Checker.check():
			pyautogui.moveTo(576, 955)
			pyautogui.dragTo(1156, 971, duration=0.5)  # drag mouse to XY
			time.sleep(0.5)
			pyautogui.hotkey('ctrl', 'c')
			time.sleep(0.2)
			ru_en[text] = (str)(pyperclip.paste())
			print("\tI don't know the answer,but at the next time i will answer: " + str(ru_en[text]))
			File_Magager.write(en_ru,'en_ru')
			pyautogui.click(1358, 967)
		else:
			pyautogui.click(1358, 967)			

	def write_smth(arr):
		print("start write somthing")
		r1 = re.sub('Напишите',"", arr)
		r1 = re.sub(' на',"", r1)
		r1 = re.sub(' английском',"", r1)
		r1 = re.sub(r'[""]',"", r1)		#choose a word
		r2 = ts.google(r1, 'ru', 'en').lower()
		
		try:
			answ = write[r1]
			print("\tI know the answer on" + str(r1) + ' is: ' + str(answ))
			pyautogui.click(928, 566)
			pyperclip.copy(answ)
			pyautogui.hotkey('ctrl', 'v')
			pyautogui.click(1362, 972)
		except KeyError:
			print("\ti trying by myslef")				
			pyautogui.click(928, 566)
			pyperclip.copy(r2)
			pyautogui.hotkey('ctrl', 'v')
			pyautogui.click(1362, 972)
		time.sleep(.5)
		if not Checker.check():
			pyautogui.moveTo(576, 955)
			pyautogui.dragTo(1156, 971, duration=0.5)  # drag mouse to XY
			time.sleep(0.5)
			pyautogui.hotkey('ctrl', 'c')
			time.sleep(0.2)
			ru_en[text] = (str)(pyperclip.paste())
			print("\tI don't know the answer,but at the next time i will answer: " + str(ru_en[text]))
			File_Magager.write(write,'write')
			pyautogui.click(1358, 967)
		else:
			pyautogui.click(1358, 967)	

class Filler:
	def fill():
		print("start filling")
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
				answ = choose2[text]
				print('\tI know the answer on "' + str(text) + '" is "' + str(answ)+ '"')
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
				pyautogui.click(1358, 967)		
		except IndexError:
				
				print(pyautogui.pixelMatchesColor(569, 900, (255, 255, 255), tolerance=2))
				print(pyautogui.pixelMatchesColor(592, 875, (255, 255, 255), tolerance=2))
				if not Checker.check():
					if (pyautogui.pixelMatchesColor(569, 900, (255, 255, 255), tolerance=2)):# 4 words
						pyautogui.moveTo(575, 902)
						pyautogui.dragTo(955, 903, duration=0.5)  # drag mouse to XY
						pyautogui.hotkey('ctrl', 'c')
						time.sleep(0.2)
						choose2[text] = (str)(pyperclip.paste())
						print("\tI don't know the answer,but at the next time i will answer: " + str(choose2[text]))
						File_Magager.write(choose2,'choose2')		
								

					elif (pyautogui.pixelMatchesColor(592, 875, (255, 255, 255), tolerance=2)): # 2 words
						pyautogui.moveTo(575, 904)
						pyautogui.dragTo(1074, 878, duration=0.5)  # drag mouse to XY
						pyautogui.hotkey('ctrl', 'c')
						time.sleep(0.2)
						choose2[text] = (str)(pyperclip.paste())
						print("\tI don't know the answer,but at the next time i will answer: " + str(choose2[text]))
						File_Magager.write(choose2,'choose2')		


					elif (pyautogui.pixelMatchesColor(569, 874, (255, 255, 255), tolerance=2)): # 6 words
						pyautogui.moveTo(583, 875)
						pyautogui.dragTo(1074, 878, duration=0.5)  # drag mouse to XY
						pyautogui.hotkey('ctrl', 'c')
						time.sleep(0.2)
						choose2[text] = (str)(pyperclip.paste())
						print("\tI don't know the answer,but at the next time i will answer: " + str(choose2[text]))
						File_Magager.write(choose2,'choose2')
																
					pyautogui.click(1356, 928)			
				else:
					choose2[text] = result3[0]
					print("\tI don't know the answer,but at the next time i will answer: " + str(choose2[text]))
					File_Magager.write(choose2,'choose2')		
					pyautogui.click(1356, 928)
				
		except KeyError:							# если есть нет в списке
				
				pyautogui.click(829, 586)
				pyautogui.click(1362, 972)
				time.sleep(.5)
				if (pyautogui.pixelMatchesColor(1782, 971, (255, 193, 193), tolerance=2)): # проверка на ошибки 
					if (pyautogui.pixelMatchesColor(569, 900, (255, 255, 255), tolerance=2)):# 4 words
						pyautogui.moveTo(575, 902)
						pyautogui.dragTo(955, 903, duration=0.5)  # drag mouse to XY
						pyautogui.hotkey('ctrl', 'c')
						time.sleep(0.2)
						choose2[text] = (str)(pyperclip.paste())
						print("\tI don't know the answer,but at the next time i will answer: " + str(choose2[text]))
						File_Magager.write(choose2,'choose2')		
					elif (pyautogui.pixelMatchesColor(592, 875, (255, 255, 255), tolerance=2)): # 2 words
						pyautogui.moveTo(575, 904)
						pyautogui.dragTo(1074, 878, duration=0.5)  # drag mouse to XY
						pyautogui.hotkey('ctrl', 'c')
						time.sleep(0.2)
						choose2[text] = (str)(pyperclip.paste())
						print("\tI don't know the answer,but at the next time i will answer: " + str(choose2[text]))
						File_Magager.write(choose2,'choose2')		
					elif (pyautogui.pixelMatchesColor(569, 874, (255, 255, 255), tolerance=2)): # 2 words
						pyautogui.moveTo(583, 875)
						pyautogui.dragTo(1074, 878, duration=0.5)  # drag mouse to XY
						pyautogui.hotkey('ctrl', 'c')
						time.sleep(0.2)
						choose2[text] = (str)(pyperclip.paste())
						print("\tI don't know the answer,but at the next time i will answer: " + str(choose2[text]))
						File_Magager.write(choose2,'choose2')										
					pyautogui.click(1356, 928)			
				else:
					choose2[text] = result3[0]
					print("\tI don't know the answer,but at the next time i will answer: " + str(choose2[text]))
					File_Magager.write(choose2,'choose2')		
					pyautogui.click(1356, 928)				
			pyautogui.click(1334, 940)					

def start():
	File_Magager.load(en_ru,'en_ru')
	File_Magager.load(ru_en,'ru_en')
	File_Magager.load(choose3,'choose3')
	File_Magager.load(choose2,'choose2')
	File_Magager.load(write,'write')

	print("start cycle")
	while True:
		time.sleep(1)
		Distributor.next_lesson()					
		Distributor.next_qustion()
	return


start()
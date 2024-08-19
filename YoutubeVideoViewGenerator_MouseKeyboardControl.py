print('it begins...')

import pyautogui
import time
import random


for x in range(4):

	time.sleep(5)
	pyautogui.click(100, 650)
	pyautogui.hotkey('enter')
	time.sleep(5)
	pyautogui.hotkey('alt', 'shift', 'n')
	time.sleep(10)


	pyautogui.write('www.youtube.com')
	pyautogui.hotkey('enter')
	time.sleep(25)


	pyautogui.click(800, 125)
	time.sleep(2)
	pyautogui.write('lofi cat buddy')
	pyautogui.hotkey('enter')
	time.sleep(5)
	pyautogui.click(400, 400)
	time.sleep(2)
	pyautogui.scroll(-1000)
	time.sleep(1)
	pyautogui.scroll(-1000)
	time.sleep(1)
	pyautogui.scroll(-1000)
	time.sleep(2)
	pyautogui.scroll(3000)
	time.sleep(2)


	pyautogui.click(1600, 300)
	time.sleep(5)
	pyautogui.click(0, 400+round(random.uniform(0, 1)*100,0))


	for y in range(29):
		time.sleep(60)
		print(y+1,' viewing minute in iternation ',x+1,' has completed')

	pyautogui.click(0, 400+round(random.uniform(0, 1)*100,0))
	time.sleep(round(random.uniform(0, 1)*100,0))


	pyautogui.hotkey('alt', 'f4')
	time.sleep(4)
	pyautogui.hotkey('alt', 'f4')


	for z in range(5):
		time.sleep(60)
		print(z+1,' intermission minute in iternation ',x+1,' has completed')
	
	time.sleep(round(random.uniform(0, 1)*100,0))

	print('iternation number ',x+1,' has completed')



# import pyautogui
# import time

# pyautogui.click(400, 400)
# time.sleep(2)
# pyautogui.scroll(-1000)
# pyautogui.scroll(-1000)
# pyautogui.scroll(-1000)
# time.sleep(2)
# pyautogui.scroll(3000)


# x = 1
# y = 2
# z = 3

# print(y,' viewing minute in iternation ',x,' has completed')
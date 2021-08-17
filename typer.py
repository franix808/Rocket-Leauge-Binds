from typing import Text
import pyautogui
from time import sleep

pyautogui.alert(text='Program should work now', title='Program is woking now', button='OK')

sleep(2)

def sraken_pierdaken():
    pyautogui.keyDown('t')
    pyautogui.keyUp('t')
    # pyautogui.write('t')
    pyautogui.write('sraken pierdaken', interval=0.08)
    pyautogui.press('enter')

# if pyautogui.press('5'):
#     sraken_pierdaken()



sleep(5)
pyautogui.alert(text='Program finished work', title='Finish', button='OK')
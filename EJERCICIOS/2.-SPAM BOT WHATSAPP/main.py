import pyautogui
import webbrowser as web
import time
from io import open

web.open("https://web.whatsapp.com/send?phone=+56961558125")
time.sleep(3)


archivo =  open("texto.txt","r")


for line in archivo:
    pyautogui.typewrite(line)
    pyautogui.press("enter")
    time.sleep(3)

"""
for i in range(2):
    pyautogui.typewrite("12 El hombre malo")
    pyautogui.press("enter")
"""





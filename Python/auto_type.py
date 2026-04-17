import pyautogui
from time import sleep  
sleep(5) #this will wait for 5 seconds before executing the next line of code   

for i in range(0,3):
    sleep(1)
    pyautogui.write('Hello, World!')
    pyautogui.press('enter') #this will press the enter key after writing the message


import pyautogui as py
import time 

message  = "I Love You"
count = 1

time.sleep(3)

for i in range(100):
    py.typewrite(message + " " + str(count))
    py.press('Enter')
    count = count + 1

py.typewrite("I Love You 3000")
py.press('Enter')
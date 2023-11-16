import pyautogui
import time

while True:
    print("moving now!")
    pyautogui.moveRel(100, 0)
    pyautogui.moveRel(-100, 0)
    time.sleep(1)
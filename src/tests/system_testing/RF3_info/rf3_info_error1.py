import pyautogui
import time
import pyperclip
import os
from rf3_utils import oracle_failure

commandButton = "command" if os.name == "posix" else "ctrl"
    
time.sleep(2)

x, y = pyautogui.position()
pyautogui.write("ddddddddddddd")
pyautogui.hotkey("enter")

screen_width, screen_height = pyautogui.size()

center_x = screen_width // 2
center_y = screen_height // 2

pyautogui.moveTo(center_x, center_y)
pyautogui.click()
pyautogui.hotkey(commandButton, "a")
pyautogui.hotkey(commandButton, "c")

contenuto_appunti = pyperclip.paste()

assert contenuto_appunti == oracle_failure


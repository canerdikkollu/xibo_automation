import os, time
import pyperclip, subprocess, pyautogui

path = '/home/svrn/snap/savron-player/x1/savron-lib'
try:
    os.mkdir(path)
except OSError as error:
    print(error)
  
cmd = "/snap/bin/savron-player.options"
subprocess.Popen(cmd)

currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX)
print(currentMouseY) 

time.sleep(3)
pyautogui.moveTo(300, 130)
pyautogui.click()
pyautogui.hotkey("ctrl", "a")

# savron-player cms-address
pyperclip.copy("http://10.0.25.22:4038")
pyautogui.hotkey("ctrl", "v")

# savron-player server key
pyautogui.press("tab")
pyperclip.copy("sEleBaOh")
pyautogui.hotkey("ctrl", "v")

# savron-player path
pyautogui.press("tab")
pyperclip.copy(path)
pyautogui.hotkey("ctrl", "v")

# savron-player save button
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")

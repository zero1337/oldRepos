import time
import keyboard
import os

def repeat(func1, n):         #func repeats n times
    if n<=0:
        return
    else:
        func1()             
        repeat(func1, n-1)
        
def tabit():                               #tab then sleep to register
    keyboard.press_and_release('tab')
    time.sleep(0.25)
    
os.startfile('C:\\Program Files\\Firefox Developer Edition\\firefox.exe')
time.sleep(6)

keyboard.press_and_release('alt+d')
time.sleep(0.5)

keyboard.write('about:debugging#/runtime/this-firefox')
time.sleep(0.25)

keyboard.press_and_release('enter')
time.sleep(3)

repeat(tabit, 6)

keyboard.press_and_release('enter')
time.sleep(2)

keyboard.press_and_release('alt+d')
time.sleep(0.1)

keyboard.write('C:\ytdlPS')
time.sleep(1.15)

keyboard.press_and_release('enter')
time.sleep(1.5)

repeat(tabit, 6)

keyboard.write('manifest.json')
time.sleep(0.2)

keyboard.press_and_release('tab')
time.sleep(1)

keyboard.press_and_release('space')
time.sleep(1)

keyboard.press_and_release('ctrl+t')
time.sleep(0.5)


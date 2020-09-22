import pyautogui
from time import sleep
import keyboard

pause = False

print(pause)

def change():
    global pause
    pause = not pause
    print(pause)

keyboard.add_hotkey('page up', lambda: change())
keyboard.add_hotkey('esc', lambda: exit())
while 1:

    
    if pause == True:
        find = pyautogui.locateOnScreen('Assets/find.png',confidence=0.9)

        if find != None:
            find_location = pyautogui.center(find)
            pyautogui.click(x=find_location.x,y=find_location.y)
            sleep(1)
            pyautogui.moveTo(100, 200)
        
        accept = pyautogui.locateOnScreen('Assets/accept.png',confidence=0.9)

        if accept != None:
            accept_location = pyautogui.center(accept)
            pyautogui.click(x=accept_location.x,y=accept_location.y)
            sleep(5)
            pyautogui.moveTo(100, 200)

        _exit = pyautogui.locateOnScreen('Assets/exit.png',confidence=0.9)

        if _exit != None:
            _exit_location = pyautogui.center(_exit)
            pyautogui.moveTo(_exit_location.x,_exit_location.y)
            pyautogui.mouseDown()
            sleep(0.5)
            pyautogui.mouseUp()
            sleep(2)
            pyautogui.moveTo(100,200)
            sleep(0.5)

        buy = pyautogui.locateOnScreen('Assets/buy.png',confidence = 0.9)

        if buy != None:
            buy_location = pyautogui.center(buy)
            pyautogui.moveTo(buy_location.x,buy_location.y-50)
            sleep(1)
            pyautogui.mouseDown()
            sleep(0.5)
            pyautogui.mouseUp()
            sleep(5)
            pyautogui.moveTo(143,234)

        ok = pyautogui.locateOnScreen('Assets/ok.png',confidence = 0.9)

        if ok != None:
            ok_location = pyautogui.center(ok)
            pyautogui.moveTo(ok_location.x,ok_location.y)
            sleep(1)
            pyautogui.mouseDown()
            sleep(0.5)
            pyautogui.mouseUp()
            sleep(2)
            pyautogui.moveTo(143,234)

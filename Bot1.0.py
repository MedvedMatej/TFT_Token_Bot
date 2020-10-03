import pyautogui
from time import sleep
import keyboard

class TFT_Bot():
    def __init__(self,hotkey):
        self.running = False
        print("Status: not running")
        keyboard.add_hotkey(hotkey,lambda : self._statusChange())

    def _statusChange(self):
        self.runnning = not self.running
        if self.running:
            print("Status: Running")
        else:
            print("Status: Not running")

    def returnStatus(self):
        return self.running

    def _click(self,x,y):
        pyautogui.moveTo(x,y)
        sleep(0.1)
        pyautogui.mouseDown()
        sleep(0.5)
        pyautogui.mouseUp()
        sleep(0.1)
        pyautogui.moveTo(1,1)
    
    def _locateImages(self):
        #find match, play, play again
        try:
            x,y = pyautogui.locateCenterOnScreen('Assets/findMatch.png',confidence=0.9,grayscale=True)
            self._click(x,y)

        except ImageNotFoundException:
            pass
        
        #accept match
        try:
            x,y = pyautogui.locateCenterOnScreen('Assets/acceptMatch.png',confidence=0.9,grayscale=True)
            self._click(x,y)

        except ImageNotFoundException:
            pass

        #annoying mission complete OK button
        try:
            x,y = pyautogui.locateCenterOnScreen('Assets/ok.png',confidence=0.9,grayscale=True)
            self._click(x,y)

        except ImageNotFoundException:
            pass

        #exit game
        try:
            x,y = pyautogui.locateCenterOnScreen('Assets/exitGame.png',confidence=0.9,grayscale=True)
            self._click(x,y)

        except ImageNotFoundException:
            pass
        
        #buy unit
        try:
            x,y = pyautogui.locateCenterOnScreen('Assets/buyUnit.png',confidence=0.9,grayscale=True)
            self._click(x,y)

        except ImageNotFoundException:
            pass


def main():
    x = TFT_Bot('page up')

    while True:
        if x.returnStatus:
            x._locateImages()


if __name__=="__main__": 
    main()
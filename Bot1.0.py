import pyautogui
from time import sleep
import keyboard

class TFT_Bot():
    def __init__(self,hotkey):
        self.running = False
        print("Status: Not running")
        keyboard.add_hotkey(hotkey,lambda : self._statusChange())

    def _statusChange(self):
        self.running = not self.running
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
    
    def _locateImage(self,imageName):
        image = "Assets/" + imageName + ".png"
        try:
            x,y = pyautogui.locateCenterOnScreen(image,confidence=0.9,grayscale=True)
            self._click(x,y)

        except TypeError:
            pass
 

def main():
    x = TFT_Bot('page up')

    while True:
        if x.returnStatus():
            x._locateImage('acceptMatch')
            x._locateImage('findMatch')
            x._locateImage('buyUnit')
            x._locateImage('exitGame')
            x._locateImage('ok')


if __name__=="__main__": 
    main()
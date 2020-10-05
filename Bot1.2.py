import pyautogui
from time import sleep
import keyboard
from itertools import cycle

class TFT_Bot():
    def __init__(self,hotkey):
        keyboard.add_hotkey(hotkey,lambda : self._statusChange())
        print("Status: Not running")
        self.running = False
        self.stages = ['findMatch','acceptMatch','buyUnit','exitGame']
        self.cycle = cycle(self.stages)
        self.currentStage = next(self.cycle)
        self.nextStage = next(self.cycle)
        self.printStages()

    def _statusChange(self):
        self.running = not self.running
        if self.running:
            print("Status: Running")
        else:
            print("Status: Not running")

    def printStages(self):
        print("Current Stage: " + self.currentStage)
        print("Next Stage: " + self.nextStage)

    def returnStatus(self):
        return self.running

    def _click(self,x,y):
        pyautogui.moveTo(x,y)
        sleep(0.1)
        pyautogui.mouseDown()
        sleep(0.5)
        pyautogui.mouseUp()
        sleep(0.1)
        pyautogui.moveTo(200,200)
    
    def _locateImage(self,imageName):
        image = "Assets/" + imageName + ".png"
        try:
            x,y = pyautogui.locateCenterOnScreen(image,confidence=0.9,grayscale=True)
            self._click(x,y)

            if(imageName == self.nextStage):
                self.currentStage = self.nextStage
                self.nextStage = next(self.cycle)

                self.printStages()

        except TypeError:
            pass
 

def main():
    x = TFT_Bot('page up')

    while True:
        if x.returnStatus():
            x._locateImage(x.currentStage)
            x._locateImage(x.nextStage)

            if(x.currentStage == "exitGame"):
                x._locateImage("ok")




if __name__=="__main__": 
    main()
import pyautogui
from time import sleep
from time import time
import keyboard
from itertools import cycle
import random

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
        self.lastAction = time()
        self.keyboard = keyboard.Controller()

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
        i = random.randint(0,5)
        j = random.randint(0,5)
        pyautogui.moveTo(x+i,y+j)
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
            self.lastAction = time()

            if(imageName == self.nextStage):
                self.currentStage = self.nextStage
                self.nextStage = next(self.cycle)

                self.printStages()

        except TypeError:
            pass
            
    def _recalibrateCurrentStage(self):
        self.currentStage = self.nextStage
        self.nextStage = next(self.cycle)


def main():
    x = TFT_Bot('page up')

    while True:
        if x.returnStatus():
            x._locateImage(x.currentStage)
            x._locateImage(x.nextStage)

            if(x.currentStage == "exitGame"):
                x._locateImage("ok")

            if(x.currentStage == "acceptMatch"):
                sleep(5)


            if(x.currentStage == "buyUnit"):
                temp = random.randint(0,25)
                if temp % 10 == 0:
                    x.keyboard.press('f')
                    x.keyboard.release('f')
                if temp % 25 == 0:
                    x.keyboard.press('d')
                    x.keyboard.release('d')
            

            if(time() - x.lastAction > 120):
                x._recalibrateCurrentStage()
        
        print(x.currentStage)



if __name__=="__main__": 
    main()
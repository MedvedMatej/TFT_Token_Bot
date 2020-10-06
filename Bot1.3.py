import pyautogui
from time import sleep
from time import time
import keyboard
from pynput.keyboard import Key, Controller
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
        self.keyboard = Controller()

    def _statusChange(self):
        self.running = not self.running
        if self.running:
            print("Status: Running")
        else:
            print("Status: Not running")

    def printStages(self):
        print("Current Stage: " + self.currentStage)
        print("Next Stage: " + self.nextStage)

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
    
    def _stageSearch(self,imageName):
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

    def _stageSpecificActions(self):
        if(self.currentStage == "exitGame"):
             self._stageSearch("ok")

        if(self.currentStage == "acceptMatch"):
            sleep(5)

        if(self.currentStage == "buyUnit"):
            #buy exp
            #refresh units
            #equip items
            pass


def main():
    x = TFT_Bot('page up')

    while True:
        if x.running:
            x._stageSearch(x.currentStage)
            x._stageSearch(x.nextStage)

            x._stageSpecificActions()

            if(time() - x.lastAction > 120):
                x._recalibrateCurrentStage()

                


if __name__=="__main__": 
    main()
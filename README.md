# TFT_Token_Bot
# What does the script do:
  1. It locates and clicks find match
  2. It locates and clicks accept match
  3. When in game it locates and buys "Cultist" units (you can change this in the assets by simply replacing the image buy.png with your prefered unit trait)
  4. When you lose it clicks on Exit now (Does not click Continue if you win, because it exits automatically anyway)
  5. In case there is a mission complete pop-up in clicks OK and continues
  6. It clicks play again
  
# How to use:
  Press "page up" button to start/pause the script. By default it starts in paused mode.
  Press "esc" to terminate the script.
  
  If you are using the console version (.py) it will display the current state of the script in the console.
  If you are using the hidden console version please note that there is no visual indication of the script's current state so keep that in mind.
  
  Under Assets folder you can find different pictures that the script is looking for on the screen. Yours may differ so in case the script is not working properly make screenshots of your own game and replace them.

## PREREQUISITES
  If you don't have all the packages that are required installed here is the list of the ones you need:    
    pip install keyboard  
    pip install wheel
    pip install pyautogui  
    pip install opencv-python

# Note:
You are using this on your own behalf. I am not held responsible for anything that may happen to your League of Legends account.

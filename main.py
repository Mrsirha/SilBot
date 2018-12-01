#The Sil Bot
import time
from sil import Sil
import random
from pynput.keyboard import Key, Controller

keyboard = Controller()

file_object = open("Sil.txt","r").read()
lines = file_object.splitlines()
print("Prepare to tpye as sil")
time.sleep(3)
i = 0
while True:
    sil = Sil(lines, time.time(), i)
    time.sleep(sil.getDeath())
    print("TPYING: " + sil.getPhrase())
    for char in sil.getPhrase():
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.001)
    time.sleep(0.1)
    keyboard.press(Key.enter)


    if sil.getInst() > 10:
        break
    i += 1
print()
print("There were " + str(sil.getInst()) + " Sils." )

#The Sil Bot
import time
from sil import Sil
import random
import keyboard as Keyboard
from pynput.keyboard import Key, Controller

keyboard = Controller()
file_object = open("Sil.txt","r").read()
lines = file_object.splitlines()

def Menu(): # A menu option (WIP - need to add functionality for Discord, input, and expected response)
    print("Welcome to SilBot \n 1.Begin typing as Sil \n 2.Exit")
    choice = input()
    if choice == "1":
        beginTyping()

    elif choice == "2":
        print("Exiting...")
        exit()

def beginTyping():
    print("Prepare to tpye as sil")
    time.sleep(3)
    i = 0
    while True:
        try:
            sil = Sil(lines, time.time(), i)
            time.sleep(sil.getDeath())
            print("TPYING: " + sil.getPhrase())
            for char in sil.getPhrase():
                keyboard.press(char)
                keyboard.release(char)
                time.sleep(0.001)
            time.sleep(0.1)
            keyboard.press(Key.enter)
            if Keyboard.is_pressed('2'):
                print("Exiting...")
                break
            i += 1
        except:
            print("There was an error...")

    print("\n There were " + str(sil.getInst()) + " Sils." )

if __name__ == '__main__':
    Menu()

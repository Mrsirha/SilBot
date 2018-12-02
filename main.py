#The Sil Bot
import time
from sil import Sil
import random
import keyboard as Keyboard
from pynput.keyboard import Key, Controller

keypress = Controller()
file_object = open("Sil.txt","r").read()
lines = file_object.splitlines()

def Menu(): # A menu option (WIP - need to add functionality for Discord, input, and expected response)
    print("Welcome to SilBot \n1.Begin typing as Sil \n2.Exit")
    choice = input("Enter: ")
    if choice == "1":
        beginTyping()

    elif choice == "2":
        print("Exiting...")
        exit()

def beginTyping():
    print("Prepare to type as sil")
    i = 0
    sil = Sil(lines, time.time(), i)
    while True:
        print(str(int(time.time())) + " >= "+ str(int(sil.getAge() + sil.getDeath())),  end='\r')
        try:
            if Keyboard.is_pressed('q'):
                print("Exiting...")
                break


            if time.time() >= sil.getAge() + sil.getDeath():
                print("TPYING: " + sil.getPhrase())
                for char in sil.getPhrase():
                    keypress.press(char)
                    keypress.release(char)
                    time.sleep(0.001)
                i += 1
                sil = Sil(lines, time.time(), i)

                time.sleep(0.1) # sometime the enter keypress does not register if it is too soon after the rest of the keypresses
                keypress.press(Key.enter)
                keypress.release(Key.enter)

        except:
            print("There was an error...")

    print("\n There were " + str(sil.getInst()) + " Sils." )

if __name__ == '__main__':
    Menu()

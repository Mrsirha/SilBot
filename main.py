#The Sil Bot
import time
import random
from sil import Sil
from difflib import SequenceMatcher
import keyboard as Keyboard
from pynput.keyboard import Key, Controller

keypress = Controller()
file_object = open("SilOld.txt","r").read()
lines = file_object.splitlines()

def Menu(): # A menu option (WIP - need to add functionality for Discord, input, and expected response)
    while True:
        print("Welcome to SilBot \nt.Begin typing as Sil \nh.ChatBot Sil\nc.convert to silspeak\nq.quit")
        choice = input("Enter: ")
        if choice == "t":
            beginTyping()
        elif choice == "h":
            silChat()
        elif choice == 'c':
            convert()
        elif choice == "q":
            quit()

        else:
            print("Invalid input")

def beginTyping():
    print("\nPrepare to type as sil")
    i = 0
    sil = Sil(lines, time.time(), i)
    while True:
        print(str(int(time.time()-sil.getAge())) + " == "+ str(int(sil.getDeath())),  end='\r')
        try:
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
            quit('e')
    print("\n There were " + str(sil.getInst()) + " Sils." )

def silChat():
    print("\nPrepare to chat with Sil!\nq:exit\n")
    sil = Sil(lines, time.time(), 0)
    sil.trainChatBot()
    while True:
        try:
            inp = input("You: ")
            if inp == 'q':
                quit()
            print("Sil: " + str(sil.getResponse(inp)))
        except:
            quit('e')

def convert():
    print("\nInput Phrase")
    sil = Sil(lines, time.time())
    out = ""
    highest = 0.0
    while True:
        try:
            inp = input("enter: ")
            if inp == "q":
                quit()
            for item in lines:
                if similar(inp,item) > highest:
                    out = item
                    highest = similar(inp,item)
                print(highest)
            print("Sil: "+out)
            out = ""
        except:
            quit('e')
def quit(char=None):
    if char == 'e':
        print("There was an error...")
        exit()
    elif type == None:
        print("Exiting...")
        exit()

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

if __name__ == '__main__':
    Menu()

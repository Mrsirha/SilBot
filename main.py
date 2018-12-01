#The Sil Bot
import time
from sil import Sil
import random

file_object = open("Sil.txt","r").read()
lines = file_object.splitlines()

while True:
    sil = Sil(lines, time.time())
    if time.time() == sil.getDeath():
        print(sil.getPhrase())
    time.sleep(1)
print("There were " + sil.getInst() + " Sils." )

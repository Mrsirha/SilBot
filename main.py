#The Sil Bot
import time
from sil import Sil
import random

file_object = open("Sil.txt","r").read()
lines = file_object.splitlines()
while True:
    sil = Sil(lines, time.time())
    time.sleep(sil.getDeath())
    print(sil.getPhrase())
    if sil.getInst() > 10:
        break

print("There were " + sil.getInst() + " Sils." )

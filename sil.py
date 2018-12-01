#the sil object that decides the phrase and time that the phrase is uttered
import random
class Sil(object):
    instance = 0 # How many sils have existed before this one
    phrases = []
    phrase = ""
    age = 0 # Time the sil was created
    death = 0
    def __init__(self, phrases, time, inst):
        self.phrases = phrases
        self.age = time
        self.instance = inst
        self.pickPhrase(phrases)
        self.pickTime()
    def pickPhrase(self,phrases):
        n = random.randint(0,len(phrases) - 1)
        self.phrase = phrases[n]
    def pickTime(self):
        # Pick a time between 0s, and 30s
        n = random.randint(1,5)
        self.death =  n
    def getAge(self):
        return self.age
    def getInst(self):
        return self.instance
    def getPhrase(self):
        return self.phrase
    def getDeath(self):
        return self.death

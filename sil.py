#the sil object that decides the phrase and time that the phrase is uttered
import random

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


class Sil(object):
    instance = 0 # How many sils have existed before this one
    phrases = []
    phrase = ""
    age = 0 # Time the sil was created
    death = 0
    input = ""
    chatbot = ChatBot("")
    def __init__(self, phrases, time, inst):
        self.phrases = phrases
        self.age = time
        self.instance = inst
        self.pickPhrase(phrases)
        self.pickTime()
        chatbot = ChatBot("Sil #"+str(self.instance))

    def pickPhrase(self,phrases):
        n = random.randint(0,len(phrases) - 1)
        self.phrase = phrases[n]

    def pickTime(self):
        # Pick a time between 0s, and 30s
        n = random.randint(0,30)
        self.death = n

    def setInput(self):
        self.input = ''

    def getAge(self):
        return self.age

    def getInst(self):
        return self.instance

    def getPhrase(self):
        return self.phrase

    def getDeath(self):
        return self.death
    def trainChatBot(self):
        self.chatbot.set_trainer(ListTrainer)
        self.chatbot.train(self.phrases)
    def getResponse(self,input):
        response = self.chatbot.get_response(input)
        return response

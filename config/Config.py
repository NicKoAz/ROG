'''
Created on 24-05-2022

@author: carol
'''

import configparser


class Config():
    
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
    def getConfig(self, dificultad):
        return dict(self.config[dificultad])

'''
config = Config()

print(config.getConfig("CONTRARELOJ-FACIL"))

print(config.getConfig("CONTRARELOJ-NORMAL"))

print(config.getConfig("CONTRARELOJ-DIFICIL"))

print(config.getConfig("MODO LIBRE-FACIL"))

print(config.getConfig("MODO LIBRE-NORMAL"))

print(config.getConfig("MODO LIBRE-DIFICIL"))
'''
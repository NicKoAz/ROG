'''
Created on 24-05-2022

@author: carol
'''

import configparser

class Config():
    
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")
    def getConfig(self):
        return (int(self.config["DIFICULTAD"]["filaFacil"]),int(self.config["DIFICULTAD"]["columnaFacil"]))

config = Config()
print(config.getConfig())
import configparser

class Config():
    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read("config.ini")
    def getConfig(self):
        return (self.config["DIFICULTAD"]["filaFacil"])
    
    
leer=Config()
print(leer.getConfig())
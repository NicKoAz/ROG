'''
Created on 21 jun 2022

@author: Nico
'''
class CuentaPares():
    def __init__(self):
        self.pares=0
        
    def SetPares(self):
        self.pares+=1
        
    def GetPares(self):
        return(self.pares)
    
    def ResetAll(self):
        self.pares=0
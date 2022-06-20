'''
Created on 20-06-2022

@author: Nicolas Carreño
'''
import wx


class CuentaPares():
    def __init__(self):
        self.pares=0
        self.bnt1=None
        self.btn2=None
        self.button1=None
        self.button2=None
        
    def SetPares(self):
        self.pares+=1
        
    def GetPares(self):
        return(self.pares)
    
    def SetBoton(self,boton):
        if self.btn1 == None:
            self.btn1=boton
        else:
            self.btn2=boton
            
    def GetBoton1(self):
        return self.btn1
    
    def getBoton2(self):
        return self.btn2
    
    def SetButton(self,button):
        if self.button1 == None:
            self.button1=button
        else:
            self.button2=button
            
    def GetButton1(self):
        return self.button1
    
    def GetButton2(self):
        return self.button2
    
    def ResetAll(self):
        self.bnt1=None
        self.btn2=None
        self.button1=None
        self.button2=None
        
               
        
    
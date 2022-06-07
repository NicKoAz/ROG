'''
Created on 16-05-2022

@author: carol
'''

import wx
from vista.VentanaModoJuego import VentanaModoDeJuego

'''
    Esto es un documento
'''

'''
Esto es una clase
'''

class VentanaPrincipal(wx.Frame):
    '''
    Este metodo es para crear 
    @param parent sirve para heredar
    '''
    def __init__(self):
        wx.Frame.__init__(self, None, title="Encontrar Los Pares", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(350, 350))
        
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(0,-7),size=(350, 350))
        self.lbl1 = wx.StaticText(self.box1,-1, 'ENCONTRAR LOS PARES', pos =(63,75))
        self.btn1 = wx.Button(self.box1, label = "INICIAR EL JUEGO", size=(150, 50), pos=(93, 125))
        self.btn2 = wx.Button(self.box1, label = "SALIR DEL JUEGO", size=(150, 50), pos=(93, 195))
        
        #Modificar Fuente
        font1=self.lbl1.GetFont()
        font1.SetPointSize(15)
        self.lbl1.SetFont(font1)        
        
        #Color fondo stacticBox
        self.box1.SetBackgroundColour("#B9D9D7")
        
        # Eventos de Botones
        self.btn1.Bind(wx.EVT_BUTTON, self.StarGame)
        self.btn2.Bind(wx.EVT_BUTTON, self.FinishGame)
        
        self.Centre(True)
    '''
    Este metodo es para 
    @param i sirve para
    '''
        
    def StarGame(self,i):
        self.Hide()
        ventanaMode=VentanaModoDeJuego(self)
        ventanaMode.ShowModal()
        ventanaMode.Destroy()
    
    '''
    Este metodo es para 
    @param i sirve para 
    '''
    
    def FinishGame(self,i):
        VentanaPrincipal()
        self.Destroy()


    
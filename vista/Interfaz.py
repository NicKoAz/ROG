'''
Created on 16-05-2022

@author: carol
'''

import wx
from vista.VentanaModoJuego import VentanaModoDeJuego

class VentanaPrincipal(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Encontrar Los Pares", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(350, 350))
        
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(10,0),size=(310, 300))
        self.lbl1 = wx.StaticText(self.box1,-1, 'ENCONTRAR LOS PARES', pos =(85,50))
        self.btn1 = wx.Button(self.box1, label = "INICIAR EL JUEGO", size=(200, 50), pos=(50, 100))
        self.btn2 = wx.Button(self.box1, label = "SALIR DEL JUEGO", size=(200, 50), pos=(50, 170))
        
        #Color Letra Botones
        self.btn1.SetForegroundColour((3, 152, 252, 255))
        self.btn2.SetForegroundColour((3, 152, 252, 255)) 

        # Eventos de Botones
        self.btn1.Bind(wx.EVT_BUTTON, self.StarGame)
        self.btn2.Bind(wx.EVT_BUTTON, self.FinishGame)

    
    def StarGame(self,i):
        self.Hide()
        ventanaMode=VentanaModoDeJuego(self)
        ventanaMode.ShowModal()
        ventanaMode.Destroy()
    
    def FinishGame(self,i):
        VentanaPrincipal()
        self.Destroy()


    
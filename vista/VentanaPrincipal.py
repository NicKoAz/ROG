'''
Created on 16-05-2022

@author: carol
'''

import wx
from vista.VentanaModosDeJuego import VentanaModosDeJuego


class VentanaPrincipal(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="Encontrar Los Pares", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(568, 400))
        
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(0,-7),size=(568, 400))
        self.lbl1 = wx.StaticText(self.box1,-1, 'ENCONTRAR LOS PARES', pos =(132,60))
        self.btn1 = wx.Button(self.box1, label = "INICIAR EL JUEGO", size=(165, 60), pos=(190, 135))
        self.btn2 = wx.Button(self.box1, label = "SALIR DEL JUEGO", size=(165, 60), pos=(190, 220))
        
        #Modificar Fuente StaticText y Button
        font1=self.lbl1.GetFont()
        font1.SetPointSize(20)
        self.lbl1.SetFont(font1)
        
        font1=self.btn1.GetFont()
        font1.SetPointSize(12)
        self.btn1.SetFont(font1) 
        
        font1=self.btn2.GetFont()
        font1.SetPointSize(12)
        self.btn2.SetFont(font1)       
        
        #Color fondo stacticBox
        self.box1.SetBackgroundColour("#B9D9D7")
        
        # Eventos de Botones
        self.btn1.Bind(wx.EVT_BUTTON, self.StarGame)
        self.btn2.Bind(wx.EVT_BUTTON, self.FinishGame)
        
        self.Centre(True)

        
    def StarGame(self,i):
        self.Hide()
        ventanaMode=VentanaModosDeJuego(self)
        ventanaMode.ShowModal()
        ventanaMode.Destroy()
    
    def FinishGame(self,i):
        VentanaPrincipal()
        self.Destroy()


    
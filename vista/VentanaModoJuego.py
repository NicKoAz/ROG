'''
Created on 24-05-2022

@author: carol
'''

import wx
from vista.VentanaDificultad import VentanaNivelDificultad

class VentanaModoDeJuego(wx.Dialog):
    def __init__ (self, parent):
        wx.Dialog.__init__(self, parent, wx.NewId(), title = "Modos De Juego", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(350, 350))
        
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(10,0),size=(310, 300))
        self.lbl1 = wx.StaticText(self.box1, -1, 'MODOS DE JUEGO', pos =(100,50))
        self.btn1 = wx.Button(self.box1, label = "CONTRARELOJ", size=(200, 50), pos=(50, 100))
        self.btn2 = wx.Button(self.box1, label = "MODO LIBRE", size=(200, 50), pos=(50, 170))
        
        #Color Letra Botones
        self.btn1.SetForegroundColour((3, 152, 252, 255))
        self.btn2.SetForegroundColour((3, 152, 252, 255)) 
        
        # Eventos de Botones
        self.btn1.Bind(wx.EVT_BUTTON, self.ModeContraReloj)
        self.btn2.Bind(wx.EVT_BUTTON, self.ModeLibre)
    
    def ModeContraReloj(self,i):
        self.Hide()
        ventanaContraReloj=VentanaNivelDificultad(self)
        ventanaContraReloj.ShowModal()
        ventanaContraReloj.Destroy()
    
    def ModeLibre(self,i):
        self.Hide()
        ventanaModoLibre=VentanaNivelDificultad(self)
        ventanaModoLibre.ShowModal()
        ventanaModoLibre.Destroy() 

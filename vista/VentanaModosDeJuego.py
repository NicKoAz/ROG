'''
Created on 15-06-2022

@author: carol
'''

import wx
from vista.PruebaVentana import PruebaVentana

class VentanaModosDeJuego(wx.Dialog):

    def __init__ (self, parent):
        wx.Dialog.__init__(self, parent, wx.NewId(), title = "Modos De Juego", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(568, 400))
        
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(0,-7),size=(568, 400))
        self.lbl1 = wx.StaticText(self.box1, -1, 'MODOS DE JUEGO', pos =(162,50))
        
        self.btncontrareloj1 = wx.Button(self.box1, label = "CONTRARELOJ-FACIL", size=(155, 50), pos=(93, 125))
        self.btncontrareloj2 = wx.Button(self.box1, label = "CONTRARELOJ-NORMAL", size=(155, 50), pos=(93, 190))
        self.btncontrareloj3 = wx.Button(self.box1, label = "CONTRARELOJ-DIFICIL", size=(155, 50), pos=(93, 255))
        
        self.btnmodolibre1 = wx.Button(self.box1, label = "MODO LIBRE-FACIL", size=(155, 50), pos=(300, 125))
        self.btnmodolibre2 = wx.Button(self.box1, label = "MODO LIBRE-NORMAL", size=(155, 50), pos=(300, 190))
        self.btnmodolibre3 = wx.Button(self.box1, label = "MODO LIBRE-DIFICIL", size=(155, 50), pos=(300, 255))
    
        
        #Modificar Fuente
        font1=self.lbl1.GetFont()
        font1.SetPointSize(20)
        self.lbl1.SetFont(font1)
        
        #Color fondo stacticBox
        self.box1.SetBackgroundColour("#B9D9D7")   
        
        self.Centre(True)
        

        # Eventos de Botones
        self.btncontrareloj1.Bind(wx.EVT_BUTTON, self.ModoContraReloj)
        self.btncontrareloj2.Bind(wx.EVT_BUTTON, self.ModoContraReloj)
        self.btncontrareloj3.Bind(wx.EVT_BUTTON, self.ModoContraReloj)
        self.btnmodolibre1.Bind(wx.EVT_BUTTON, self.ModoLibre)
        self.btnmodolibre2.Bind(wx.EVT_BUTTON, self.ModoLibre)
        self.btnmodolibre3.Bind(wx.EVT_BUTTON, self.ModoLibre)


        self.Centre(True)

    def ModoContraReloj(self,i):
        self.Hide()
        ventanaContraReloj=PruebaVentana(self)
        ventanaContraReloj.ShowModal()
        ventanaContraReloj.Destroy()
    
    def ModoLibre(self,i):
        self.Hide()
        ventanaModoLibre=PruebaVentana(self)
        ventanaModoLibre.ShowModal()
        ventanaModoLibre.Destroy()
        

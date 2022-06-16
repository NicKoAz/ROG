'''
Created on 24-05-2022

@author: carol
'''

import wx
from vista.PruebaVentana import PruebaVentana

 
class VentanaNivelDificultad(wx.Dialog):
    
    def __init__ (self, parent):
        wx.Dialog.__init__(self, parent, wx.NewId(),title = "Nivel De Dificultad", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(350, 350))
        
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(0,-7),size=(350, 350))
        self.lbl1 = wx.StaticText(self.box1, -1, "NIVEL DE DIFICULTAD" , pos =(73,50))
        self.btnfacil = wx.Button(self.box1, label = "FACIL", size=(150, 50), pos=(93, 100))
        self.btnnormal = wx.Button(self.box1, label = "NORMAL", size=(150, 50), pos=(93, 160))
        self.btndificil = wx.Button(self.box1, label = "DIFICIL", size=(150, 50), pos=(93, 220))      
        
        #Modificar Fuente
        font1=self.lbl1.GetFont()
        font1.SetPointSize(15)
        self.lbl1.SetFont(font1)
        
        #Color fondo stacticBox
        self.box1.SetBackgroundColour("#B9D9D7")
        
        self.Centre(True)
        
        #Eventos de Botones
        self.btnfacil.Bind(wx.EVT_BUTTON, self.NivelFacil)
        self.btnnormal.Bind(wx.EVT_BUTTON, self.NivelNormal)
        self.btndificil.Bind(wx.EVT_BUTTON, self.NivelDificil)
        
    def NivelFacil(self,i):
        self.Hide()
        VentanaNivelDificultad=PruebaVentana(self)
        VentanaNivelDificultad.ShowModal()
        VentanaNivelDificultad.Destroy()
        
    def NivelNormal(self,i):
        self.Hide()
        VentanaNivelDificultad=PruebaVentana(self)
        VentanaNivelDificultad.ShowModal()
        VentanaNivelDificultad.Destroy()
            
    def NivelDificil(self,i):
        self.Hide()
        VentanaNivelDificultad=PruebaVentana(self)
        VentanaNivelDificultad.ShowModal()
        VentanaNivelDificultad.Destroy()
    
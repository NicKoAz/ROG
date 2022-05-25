'''
Created on 24-05-2022

@author: carol
'''

import wx

'''
    Esto es un documento
'''

##
#Esto es una clase
#
 
class VentanaNivelDificultad(wx.Dialog):
    ##
    # Este metodo es para 
    # @param parent
    #
    def __init__ (self, parent):
        wx.Dialog.__init__(self, parent, wx.NewId(), title = "Nivel De Dificultad", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(350, 350))
        
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(10,0),size=(310, 300))
        self.lbl1 = wx.StaticText(self.box1, -1, "NIVEL DE DIFICULTAD" , pos =(100,50))
        self.btn1 = wx.Button(self.box1, label = "FACIL", size=(200, 50), pos=(50, 100))
        self.btn2 = wx.Button(self.box1, label = "NORMAL", size=(200, 50), pos=(50, 170))
        self.btn3 = wx.Button(self.box1, label = "DIFICIL", size=(200, 50), pos=(50, 240))
        
        #Color Letra Botones
        self.btn1.SetForegroundColour((3, 152, 252, 255))
        self.btn2.SetForegroundColour((3, 152, 252, 255))
        self.btn3.SetForegroundColour((3, 152, 252, 255))
        
        # Eventos de Botones
        #self.btn1.Bind(wx.EVT_BUTTON, self.NivelFacil)
        #self.btn2.Bind(wx.EVT_BUTTON, self.NivelNormal)
        #self.btn3.Bind(wx.EVT_BUTTON, self.NivelDificil)

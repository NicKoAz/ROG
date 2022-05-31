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
        wx.Dialog.__init__(self, parent, wx.NewId(),title = "Nivel De Dificultad", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(350, 350))
        
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(0,-7),size=(350, 350))
        self.lbl1 = wx.StaticText(self.box1, -1, "NIVEL DE DIFICULTAD" , pos =(73,50))
        self.btn1 = wx.Button(self.box1, label = "FACIL", size=(150, 50), pos=(93, 100))
        self.btn2 = wx.Button(self.box1, label = "NORMAL", size=(150, 50), pos=(93, 160))
        self.btn3 = wx.Button(self.box1, label = "DIFICIL", size=(150, 50), pos=(93, 220))      
        
        #Modificar Fuente
        font1=self.lbl1.GetFont()
        font1.SetPointSize(15)
        self.lbl1.SetFont(font1)
        
        #Color fondo stacticBox
        self.box1.SetBackgroundColour("#0FFFFF")
        
        self.Centre(True)
        
        # Eventos de Botones
        #self.btn1.Bind(wx.EVT_BUTTON, self.NivelFacil)
        #self.btn2.Bind(wx.EVT_BUTTON, self.NivelNormal)
        #self.btn3.Bind(wx.EVT_BUTTON, self.NivelDificil)

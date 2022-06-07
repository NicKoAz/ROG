'''
Created on 24-05-2022

@author: carol
'''

import wx
from source.vista.VentanaDificultad import VentanaNivelDificultad

'''
    Esto es un documento
'''

##
#Esto es una clase
#

class VentanaModoDeJuego(wx.Dialog):
    ##
    # Este metodo es para crear
    # @param parent sirve para heredar
    #
    def __init__ (self, parent):
        wx.Dialog.__init__(self, parent, wx.NewId(), title = "Modos De Juego", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(350, 350))
        
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(0,-7),size=(350, 350))
        self.lbl1 = wx.StaticText(self.box1, -1, 'MODOS DE JUEGO', pos =(83,75))
        self.btn1 = wx.Button(self.box1, label = "CONTRARELOJ", size=(150, 50), pos=(93, 125))
        self.btn2 = wx.Button(self.box1, label = "MODO LIBRE", size=(150, 50), pos=(93, 195))
        
        #Modificar Fuente
        font1=self.lbl1.GetFont()
        font1.SetPointSize(15)
        self.lbl1.SetFont(font1)
        
        #Color fondo stacticBox
        self.box1.SetBackgroundColour("#0FFFFF")   
        
        # Eventos de Botones
        self.btn1.Bind(wx.EVT_BUTTON, self.ModeContraReloj)
        self.btn2.Bind(wx.EVT_BUTTON, self.ModeLibre)

        self.Centre(True)
    
    ##
    # Este metodo es para crear
    # @param i sirve para 
    #
    
    def ModeContraReloj(self,i):
        self.Hide()
        ventanaContraReloj=VentanaNivelDificultad(self)
        ventanaContraReloj.ShowModal()
        ventanaContraReloj.Destroy()
    
    ##
    # Este metodo es para
    # @param i sirve para
    #
    
    def ModeLibre(self,i):
        self.Hide()
        ventanaModoLibre=VentanaNivelDificultad(self)
        ventanaModoLibre.ShowModal()
        ventanaModoLibre.Destroy() 

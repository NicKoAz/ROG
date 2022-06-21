'''
Created on 21 jun 2022

@author: Nico
'''

import wx
from vista.VentanaJuego import VentanaJuego

'''

    Esto es un documento
    
'''

'''

    Esto es una clase
    
'''

class VentanaModosDeJuego(wx.Dialog):
    
    '''
    
    Clase encargada de mostrar la ventana de dialogo de los modos de juego

    :param parent: Objeto grafico padre del Dialog
    
    :type parent: wx.Dialog
    
    '''

    def __init__ (self, parent):
        
        '''
        
        Constructor de la clase VentanaModosDeJuego
        
        :param self: parametro por default
        
        :param parent: Objeto grafico padre del Dialog
        
        '''
        
        wx.Dialog.__init__(self, parent, wx.NewId(), title = "Modos De Juego", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(568, 400))
        
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(0,-7),size=(568, 400))
        self.lbl1 = wx.StaticText(self.box1, -1, 'MODOS DE JUEGO', pos =(162,50))
        
        self.btncontrarelojfacil = wx.Button(self.box1, label = "CONTRARELOJ-FACIL", size=(155, 50), pos=(93, 125))
        self.btncontrarelojnormal = wx.Button(self.box1, label = "CONTRARELOJ-NORMAL", size=(155, 50), pos=(93, 190))
        self.btncontrarelojdificil = wx.Button(self.box1, label = "CONTRARELOJ-DIFICIL", size=(155, 50), pos=(93, 255))
        
        self.btnmodolibrefacil = wx.Button(self.box1, label = "MODO LIBRE-FACIL", size=(155, 50), pos=(300, 125))
        self.btnmodolibrenormal = wx.Button(self.box1, label = "MODO LIBRE-NORMAL", size=(155, 50), pos=(300, 190))
        self.btnmodolibredificil = wx.Button(self.box1, label = "MODO LIBRE-DIFICIL", size=(155, 50), pos=(300, 255))
    
        #Modificar fuente de letra StaticText
        font1=self.lbl1.GetFont()
        font1.SetPointSize(20)
        self.lbl1.SetFont(font1)
        
        #Modificar el color de fondo del StaticBox
        self.box1.SetBackgroundColour("#B9D9D7")   
        
        #Para que la ventana se abra en el centro de la pantalla
        self.Centre(True)
        
        #Eventos de Botones
        self.btncontrarelojfacil.Bind(wx.EVT_BUTTON, self.OnClick)
        self.btncontrarelojnormal.Bind(wx.EVT_BUTTON, self.OnClick)
        self.btncontrarelojdificil.Bind(wx.EVT_BUTTON, self.OnClick)
        self.btnmodolibrefacil.Bind(wx.EVT_BUTTON, self.OnClick)
        self.btnmodolibrenormal.Bind(wx.EVT_BUTTON, self.OnClick)
        self.btnmodolibredificil.Bind(wx.EVT_BUTTON, self.OnClick)
        
        #Para que la ventana se abra en el centro de la pantalla
        self.Centre(True)
        
    def OnClick(self, event):
        
        '''
        
        Funcion encargada de guardar el nombre del boton en el que se hizo click y abrir la ventana de juego
        
        :param self: parametro por default
        
        :param event: inicializa un evento
        
        :type event: wx.EVT
        
        '''
        
        labelbotones=event.GetEventObject().GetLabel()
        self.Hide()
        
        if labelbotones=="CONTRARELOJ-FACIL":
            ventanaJuego=VentanaJuego(self,4,4,90,1)
            
        elif labelbotones=="CONTRARELOJ-NORMAL":
            ventanaJuego=VentanaJuego(self,4,5,150,1)
        
        elif labelbotones=="CONTRARELOJ-DIFICIL":
            ventanaJuego=VentanaJuego(self,4,7,120,1)
        
        elif labelbotones=="MODO LIBRE-FACIL":
            ventanaJuego=VentanaJuego(self,4,4,0,2)
            
        elif labelbotones=="MODO LIBRE-NORMAL":
            ventanaJuego=VentanaJuego(self,4,5,0,2)

        elif labelbotones=="MODO LIBRE-DIFICIL":
            ventanaJuego=VentanaJuego(self,4,7,0,2)
            
        ventanaJuego.ShowModal()
        ventanaJuego.Destroy()
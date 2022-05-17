'''
Created on 16-05-2022

@author: carol
'''

import wx

class Interfaz(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Encontrar Los Pares", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(800, 300))
        
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(10,0),size=(760, 250))
        self.lbl1 = wx.StaticText(self.box1,-1, 'ENCONTRAR LOS PARES', pos =(285,50))
        self.btn1 = wx.Button(self.box1, label = "INICIAR EL JUEGO", size=(200, 30), pos=(250, 100))
        self.btn2 = wx.Button(self.box1, label = "SALIR DEL JUEGO", size=(200, 30), pos=(250, 150))

        # Eventos de Botones
        self.btn1.Bind(wx.EVT_BUTTON, self.StarGame)
        self.btn2.Bind(wx.EVT_BUTTON, self.FinishGame)
    
    def StarGame(self,i):
        ventanaMode=VentanaModoDeJuego(self)
        ventanaMode.ShowModal()
        ventanaMode.Destroy()
        Interfaz.Destroy()
    
    def FinishGame(self,i):
        Interfaz()
        self.Destroy()

class VentanaModoDeJuego(wx.Dialog):
    def __init__ (self, parent):
        wx.Dialog.__init__(self, parent, wx.NewId(), title = "Modos De Juego", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(800, 300))
        
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(10,0),size=(760, 250))
        self.lbl1 = wx.StaticText(self.box1, -1, 'MODOS DE JUEGO', pos =(285,50))
        self.btn1 = wx.Button(self.box1, label = "CONTRARELOJ", size=(200, 30), pos=(250, 100))
        self.btn2 = wx.Button(self.box1, label = "MODO LIBRE", size=(200, 30), pos=(250, 150))
        
        # Eventos de Botones
        self.btn1.Bind(wx.EVT_BUTTON, self.ModeContrareloj)
        self.btn2.Bind(wx.EVT_BUTTON, self.ModeLibre)
    
    def ModeContrareloj(self,i):
        ventanaContrareloj=VentanaNivelDificultad(self)
        ventanaContrareloj.ShowModal()
        ventanaContrareloj.Destroy()
    
    def ModeLibre(self,i):
        ventanaModoLibre=VentanaNivelDificultad(self)
        ventanaModoLibre.ShowModal()
        ventanaModoLibre.Destroy() 


class VentanaNivelDificultad(wx.Dialog):
    def __init__ (self, parent):
        wx.Dialog.__init__(self, parent, wx.NewId(), title = "Nivel De Dificultad", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(800, 300))
        
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(10,0),size=(760, 250))
        self.lbl1 = wx.StaticText(self.box1, -1, "NIVEL DE DIFICULTAD" , pos =(285,50))
        self.btn1 = wx.Button(self.box1, label = "FACIL", size=(200, 30), pos=(250, 100))
        self.btn2 = wx.Button(self.box1, label = "NORMAL", size=(200, 30), pos=(250, 150))
        self.btn3 = wx.Button(self.box1, label = "DIFICIL", size=(200, 30), pos=(250, 200))
        
        # Eventos de Botones
        #self.btn1.Bind(wx.EVT_BUTTON, self.NivelFacil)
        #self.btn2.Bind(wx.EVT_BUTTON, self.NivelNormal)
        #self.btn3.Bind(wx.EVT_BUTTON, self.NivelDificil)

    
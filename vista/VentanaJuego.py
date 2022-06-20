'''
Created on 19-06-2022

@author: carol
'''

import wx
import random
from vista.VentanaMensaje import VentanaMensaje


def GetLabel(event):
    boton=event.GetEventObject()
    nombreboton=event.GetEventObject().GetName()
    
    print(nombreboton)

    image=wx.Image("../Cards/"+nombreboton+".png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
    boton.SetBitmap(image)


def TestNombre(event):
    print("hola")
    
filas=4
columnas=5

class VentanaJuego(wx.Dialog):

    def __init__ (self, parent):
        wx.Dialog.__init__(self, parent, wx.NewId(), title = "Memoriza", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        
        self.panel = wx.Panel(self)
        self.counter = 3
        
        #Cambiar el color de fondo 
        self.SetBackgroundColour('#B9D9D7')
        
        #Sizers
        self.grillasizer=wx.BoxSizer(wx.VERTICAL)
        self.gridsizer=wx.GridSizer(filas,columnas,3,3)
        
        #Labels
        self.lbl1 = wx.StaticText(self, label='0:00')
        fuente1 = wx.Font(17, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.lbl1.SetFont(fuente1)
        
        self.lbltiempo = wx.StaticText(self, label='Tiempo Restante')
        fuente2=self.lbltiempo.GetFont()
        fuente2.SetPointSize(15)
        self.lbltiempo.SetFont(fuente2)
        
        #Botones
        self.btn1 = wx.Button(self, wx.ID_ANY, label='Iniciar Partida', size=(150, 25))
        self.btn1.Bind(wx.EVT_BUTTON, self.InicioReloj)
        
        #Timer
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.TerminoReloj, self.timer)
        
        #Randomizador de la grilla
        rdm=random.sample(range(1,20),10)
        rdm.extend(rdm)
        random.shuffle(rdm)
        print(rdm)
        
        #Agregando sizer
        for i in (rdm):
            imagefile=wx.Image("../Cards/back.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
            btn=str(i)
            self.gridsizer.Add(wx.BitmapButton(self,name=btn,bitmap=imagefile, size= (imagefile.GetWidth(), imagefile.GetHeight() )),-1,wx.ALL|wx.ALIGN_CENTER,border=2)
            self.Bind(wx.EVT_BUTTON,GetLabel)
        
        #Configuracion sizer
        self.grillasizer.Add(self.gridsizer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, border=10)
        self.grillasizer.Add(self.lbltiempo,0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, border=0)
        self.grillasizer.Add(self.lbl1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, border=0)
        self.grillasizer.Add(self.btn1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, border=0)
        self.SetSizer(self.grillasizer)
        
        #Maximizar la ventana
        self.Maximize(True)
        
        #Se muestra todo a la vez
        self.Show()

    def InicioReloj(self, e):
        self.timer.Start(1000)

    def TerminoReloj(self, e):
        if self.counter == -1: #0
            self.timer.Stop()
            self.Hide()
            ventanaMensaje=VentanaMensaje(self)
            ventanaMensaje.ShowModal()
            return
        else:
            minutos = self.counter // 60
            segundos = self.counter - (minutos * 60)
            self.counter -= 1
        self.lbl1.SetLabel(f"{str(minutos)}:{str(segundos)}")
        #self.TimeLabelCounter = wx.StaticText(self, label=f"{minutos:02}:{segundos:02}")


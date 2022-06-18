'''
Created on 14-06-2022

@author: carol
'''

import wx
import time
import random
from wx import ALIGN_CENTER


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
        wx.Dialog.__init__(self, parent, wx.NewId(), title = "Encontrar Los Pares", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(568, 400))
        
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(0,-7),size=(568, 400))
        
        #Grilla
        
        #Randomizador de la grilla 
        self.vsizer=wx.BoxSizer(wx.VERTICAL)      
        rdm=random.sample(range(1,20),10)
        rdm.extend(rdm)
        random.shuffle(rdm)
        print(rdm)
       
        self.gridsizer=wx.GridSizer(filas,columnas,3,3)

        for i in (rdm):
            imagefile=wx.Image("../Cards/back.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
            btn=str(i)
            self.gridsizer.Add(wx.BitmapButton(self,name=btn,bitmap=imagefile, size= (imagefile.GetWidth(), imagefile.GetHeight() )),-1,wx.ALL|wx.ALIGN_CENTER,border=2)
            self.Bind( wx.EVT_BUTTON,GetLabel)
            
        self.vsizer.Add(self.gridsizer,-1,wx.ALIGN_CENTER|wx.ALL, border=10)
        self.SetSizer(self.vsizer)  
        

        #Modificar color de fondo del StaticBox
        self.box1.SetBackgroundColour('#B9D9D7')
        self.panel.SetBackgroundColour('#B9D9D7')
        
        #Para que la ventana se abra en el centro de la pantalla
        self.Centre(True)
        
        #Para que la ventana se maximize
        self.Maximize(True)
        
        #ContraReloj
        self.counter = 300

        fuente = wx.Font(24, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        self.lbl = wx.StaticText(self.box1,-1, 'Inicio')
        self.lbl.SetFont(fuente)
        
        self.btn = wx.Button(self.box1, label='Comienza a Contar')
        self.btn.Bind(wx.EVT_BUTTON, self.InicioReloj)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.TerminoReloj, self.timer)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lbl, 0, wx.ALL|wx.ALIGN_RIGHT, 10)
        sizer.Add(self.btn, 0, wx.ALL|wx.ALIGN_RIGHT, 10)
        self.panel.SetSizer(sizer)

        self.Show()

    def InicioReloj(self, e):
        self.timer.Start(1000)

    def TerminoReloj(self, event):
        if self.counter == 0:
            self.timer.Stop()
            self.lbl.SetLabel('El juego ha terminado')
            return
        else:
            minutos = self.counter // 60
            segundos = self.counter - (minutos * 60)
            self.counter -= 1

        self.lbl.SetLabel(f"{str(minutos)}:{str(segundos)}")




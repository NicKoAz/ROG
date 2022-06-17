'''
Created on 14-06-2022

@author: carol
'''

import wx

class PruebaVentana(wx.Dialog):

    def __init__ (self, parent):
        wx.Dialog.__init__(self, parent, wx.NewId(), title = "Grilla", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(350, 350))
        
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(0,-7),size=(350, 350))
        self.lbl1 = wx.StaticText(self.box1, -1, 'Supuesta ventana Grilla', pos =(83,75))
        
        #Modificar fuente de letra StaticText
        font1=self.lbl1.GetFont()
        font1.SetPointSize(15)
        self.lbl1.SetFont(font1)
        
        #Modificar color de fondo del StaticBox
        self.box1.SetBackgroundColour("#B9D9D7")
        
        #Para que la ventana se abra en el centro de la pantalla
        self.Centre(True)

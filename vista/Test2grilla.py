import wx
import random
from wx import ALIGN_CENTER


def GetLabel(event):
    nombreboton=event.GetEventObject().GetName()
    print(nombreboton)
    


def TestNombre(event):
    print("hola")
    
filas=4
columnas=4
#'''MyPanel: Clase  que contiene  a la grilla'''
class MyPanel(wx.Panel):
    def __init__(self,parent):
        super(MyPanel,self).__init__(parent)
#'''Randomizador de la grilla'''        
        rdm=random.sample(range(1,30),8)
        rdm.extend(rdm)
        random.shuffle(rdm)
        print(rdm)
        vbox=wx.BoxSizer(wx.VERTICAL)
        hbox=wx.BoxSizer(wx.HORIZONTAL)
       
        gridsizer=wx.GridSizer(filas,columnas,3,3)
        #for i in range(1,17):
        for i in (rdm):
            #btn="btn"+ str(i)
            imagefile=wx.Image("../Cards/1.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
            btn=str(i)
            gridsizer.Add(wx.BitmapButton(self,name=btn,bitmap=imagefile),-1,wx.EXPAND)     #era0envezde-1
            self.SetSizer(gridsizer)
            self.Bind( wx.EVT_BUTTON,GetLabel)
            
            
            self.btn=wx.BitmapButton(self,id= -1)
            
           
    #wx.EXPAND
        

class MyFrame(wx.Frame):
    
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,"grilla", size=(600,400))
        
        
        panel=MyPanel(self)
        
if __name__=="__main__" :
    app=wx.App()
    frame=MyFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()      
    
    



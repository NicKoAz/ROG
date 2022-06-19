import wx
import random


def GetLabel(event):
    boton=event.GetEventObject()#.GetName()
    nombreboton=event.GetEventObject().GetName()
    
    print(nombreboton)
    #nombreboton.
    image=wx.Image("../Cards/"+nombreboton+".png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
    boton.SetBitmap(image)


def TestNombre(event):
    print("hola")
    
filas=4
columnas=5

#'''MyPanel: Clase  que contiene  a la grilla'''
class MyPanel(wx.Panel):
    def __init__(self,parent):
        super(MyPanel,self).__init__(parent)
        
#'''Randomizador de la grilla'''  
        self.vsizer=wx.BoxSizer(wx.VERTICAL)      
        rdm=random.sample(range(1,20),10)
        rdm.extend(rdm)
        random.shuffle(rdm)
        print(rdm)
        #vbox=wx.BoxSizer(wx.VERTICAL)
        #hbox=wx.BoxSizer(wx.HORIZONTAL)
       
        self.gridsizer=wx.GridSizer(filas,columnas,3,3)
        #for i in range(1,17):
        for i in (rdm):
            #btn="btn"+ str(i)
            imagefile=wx.Image("../Cards/back.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
            btn=str(i)
            self.gridsizer.Add(wx.BitmapButton(self,name=btn,bitmap=imagefile, size= (imagefile.GetWidth(), imagefile.GetHeight() )),-1,wx.ALL|wx.ALIGN_CENTER,border=2)     #era0envezde-1
            
           
            self.Bind( wx.EVT_BUTTON,GetLabel)
        #self.SetSizerAndFit(self.gridsizer)   
            #self.Centre()
        self.vsizer.Add(self.gridsizer,-1,wx.ALIGN_CENTER|wx.ALL, border=10)
        self.SetSizer(self.vsizer)  
            #self.btn=wx.BitmapButton(self,id= -1)
            
           
    #wx.EXPAND
        

class MyFrame(wx.Frame):
    
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,"grilla",size=(700,600))
        self.Maximize(True)
        self.SetBackgroundColour('#B9D9D7')
        panel=MyPanel(self)
        
if __name__=="__main__" :
    app=wx.App()
    frame=MyFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()      
    
    



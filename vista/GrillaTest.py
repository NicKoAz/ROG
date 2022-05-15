import wx
import random



filas=4
columnas=4

class MyPanel(wx.Panel):
    def __init__(self,parent):
        super(MyPanel,self).__init__(parent)
        
        rdm=random.sample(range(1,100),8)
        rdm.extend(rdm)
        random.shuffle(rdm)
        print(rdm)
        
        gridsizer=wx.GridSizer(filas,columnas,3,3)
        #for i in range(1,17):
        for i in (rdm):
            #btn="btn"+ str(i)
            btn=str(i)
            gridsizer.Add(wx.Button(self, label=btn),0,wx.EXPAND)
            self.SetSizer(gridsizer)
            
            
        

class MyFrame(wx.Frame):
    
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,"grilla", size=(600,400))
        
        
        panel=MyPanel(self)
        
if __name__=="__main__" :
    app=wx.App()
    frame=MyFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()       
    
    


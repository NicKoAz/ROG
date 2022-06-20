import wx
import random


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

    def __init__ (self,parent,filas,columnas, tiempo):
        wx.Dialog.__init__(self, parent, wx.NewId(), title = "Encontrar Los Pares", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        
        self.panel = wx.Panel(self)
        self.counter = int(tiempo)
        
        self.filas=int(filas)
        self.columnas=int(columnas)
        self.par=int((self.filas*self.columnas)/2)
        #Cambiar el color de fondo 
        self.SetBackgroundColour('#B9D9D7')

        #Grilla
        
        #Sizers
        
        self.grillasizer=wx.BoxSizer(wx.VERTICAL)
        self.relojsizer=wx.BoxSizer(wx.VERTICAL)
        self.gridsizer=wx.GridSizer(self.filas,self.columnas,3,3)
        
        
        
        #Labels
        fuente = wx.Font(24, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.lbl1 = wx.StaticText(self,-1, 'Inicio')
        self.lbl1.SetFont(fuente)
        
        #Botones
        self.btn1 = wx.Button(self, label='Comienza a Contar')
        self.btn1.Bind(wx.EVT_BUTTON, self.InicioReloj)
        
        #Timer
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.TerminoReloj, self.timer)
        
        #Randomizador de la grilla
        rdm=random.sample(range(1,20),self.par)
        rdm.extend(rdm)
        random.shuffle(rdm)
        print(rdm)
        
        #Agregando sizer
        for i in (rdm):
            imagefile=wx.Image("../Cards/back.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
            btn=str(i)
            self.gridsizer.Add(wx.BitmapButton(self,name=btn,bitmap=imagefile, size= (imagefile.GetWidth(), imagefile.GetHeight() )),-1,wx.ALL|wx.ALIGN_CENTER,border=2)
            self.Bind(wx.EVT_BUTTON,GetLabel)
        
        for obj in (self.lbl1, self.btn1, ):
            self.relojsizer.Add(obj, 1, wx.EXPAND|wx.ALL, 2)
            obj.SetInitialSize((0,0))
            
        #Configuracion sizer
        self.grillasizer.Add(self.gridsizer,-1,wx.ALIGN_CENTER|wx.ALL, border=10)
        self.grillasizer.Add(self.relojsizer, -1, wx.EXPAND|wx.ALL, 10) 
        self.SetSizer(self.grillasizer)
        
        #Maximizar la ventana
        self.Maximize(True)
        
        self.Show()
        

    def InicioReloj(self, e):
        self.timer.Start(1000)

    def TerminoReloj(self, event):
        if self.counter == 0:
            self.timer.Stop()
            self.lbl1.SetLabel('El juego ha terminado')
            return
        else:
            minutos = self.counter // 60
            segundos = self.counter - (minutos * 60)
            self.counter -= 1

        self.lbl1.SetLabel(f"{str(minutos)}:{str(segundos)}")


        
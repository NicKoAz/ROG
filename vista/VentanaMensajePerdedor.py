'''
Created on 21 jun 2022

@author: Nico
'''
import wx

##Esto es la clase VentanaMensajePerdedor encargada de mostrar la ventana de dialogo del mensaje perdedor
#

class VentanaMensajePerdedor(wx.Dialog):
    
    ##Este es el constructor de la clase VentanaMensajePerdedor
    # @param parent Objeto grafico padre del Dialog
    #

    def __init__ (self, parent):
        wx.Dialog.__init__(self, parent, wx.NewId(), title = "Mensaje", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(600, 200))
        
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(0,-7),size=(600, 200))
        self.lbl1 = wx.StaticText(self.box1, -1, label='Lo siento, no encontraste todos los pares :(', pos =(40,50))
        
        self.btnsalir = wx.Button(self.box1, label = 'Salir', size=(100, 25), pos=(245, 100))
        
        #Modificar fuente de letra StaticText
        font1=self.lbl1.GetFont()
        font1.SetPointSize(20)
        self.lbl1.SetFont(font1)
        
        #Modificar el color de fondo del StaticBox
        self.box1.SetBackgroundColour("#B9D9D7")   
        
        #Eventos de Botones
        self.btnsalir.Bind(wx.EVT_BUTTON, self.FinDePartida)

        #Para que la ventana se abra en el centro de la pantalla
        self.Centre(True)
        
    ##Funcion encargada de cerrar la VentanaMensajePerdedor
    # @param i Inicializa un evento
    #  
    def FinDePartida(self, i):
        VentanaMensajePerdedor(self)
        self.Destroy()
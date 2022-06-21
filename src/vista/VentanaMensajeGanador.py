'''
Created on 21 jun 2022

@author: Nico
'''

import wx

'''

    Esto es un documento
    
'''

'''

    Esto es una clase
    
'''

class VentanaMensajeGanador(wx.Dialog):
    
    '''
    
    Clase encargada de mostrar la ventana de dialogo del mensaje perdedor

    :param parent: Objeto grafico padre del Dialog
    
    :type parent: wx.Dialog
    
    '''


    def __init__ (self, parent):
                
        '''
        
        Constructor de la clase VentanaMesajePerdedor
        
        :param self: Parametro por default
        
        :param parent: Objeto grafico padre del Dialog
        
        '''
        
        wx.Dialog.__init__(self, parent, wx.NewId(), title = "Mensaje", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(600, 200))
        
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(0,-7),size=(600, 200))
        self.lbl1 = wx.StaticText(self.box1, -1, label='Felicidades!!! Encontraste todos los pares :)', pos =(40,50))
        
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
        
    def FinDePartida(self, i):
        
        '''
        
        Funcion encargada de cerrar la VentanaMensajeGanador
        
        :param self: Parametro por default
        
        :param i: Inicializa un evento
        
        '''
        
        VentanaMensajeGanador(self)
        self.Destroy()
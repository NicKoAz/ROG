'''
Created on 21 jun 2022

@author: Nico
'''

import wx
from vista.VentanaModosDeJuego import VentanaModosDeJuego


'''

    Esto es un documento
    
'''

'''

    Esto es una clase
    
'''

class VentanaPrincipal(wx.Frame):
    
    '''
    
    Clase encargada de mostrar la ventana principal del juego
    
    '''

    def __init__(self):
        
        '''
        
        Este es el constructor de la clase VentanaPrincipal
        
        :param self: parametro por default
        
        '''
        
        wx.Frame.__init__(self, None, title="Encontrar Los Pares", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX),size=(568, 400))
        
        self.panel = wx.Panel(self)
        
        self.box1 = wx.StaticBox(self.panel, wx.ID_ANY, pos=(0,-7),size=(568, 400))
        
        self.lbl1 = wx.StaticText(self.box1,-1, 'ENCONTRAR LOS PARES', pos =(132,60))
        self.btniniciarjuego = wx.Button(self.box1, label = "INICIAR EL JUEGO", size=(165, 60), pos=(190, 135))
        self.btnsalirjuego = wx.Button(self.box1, label = "SALIR DEL JUEGO", size=(165, 60), pos=(190, 220))
        
        #Modificar fuente de letra StaticText
        font1=self.lbl1.GetFont()
        font1.SetPointSize(20)
        self.lbl1.SetFont(font1)
        
        #Modificar fuente de letra Button Iniciar Juego
        font1=self.btniniciarjuego.GetFont()
        font1.SetPointSize(12)
        self.btniniciarjuego.SetFont(font1) 
        
        #Modificar fuente de letra Button Salir Juego
        font1=self.btnsalirjuego.GetFont()
        font1.SetPointSize(12)
        self.btnsalirjuego.SetFont(font1)       
        
        #Modificar color de fondo del StaticBox
        self.box1.SetBackgroundColour("#B9D9D7")
        
        #Eventos de Botones
        self.btniniciarjuego.Bind(wx.EVT_BUTTON, self.InicioJuego)
        self.btnsalirjuego.Bind(wx.EVT_BUTTON, self.FinDelJuego)
        
        #Para que la ventana se abra en el centro de la pantalla
        self.Centre(True)

        
    def InicioJuego(self,i):
        
        '''
        
        Funcion encargada de mostrar en pantalla la VentanaModosDeJuego
        
        :param self: parametro por default
        
        :param i: inicializa un evento
        
        '''
        
        self.Hide()
        ventanaMode=VentanaModosDeJuego(self)
        ventanaMode.ShowModal()
        ventanaMode.Destroy()
    
    def FinDelJuego(self,i):
        
        '''
        
        Funcion encargada de cerrar la VentanaPrincipal
        
        :param self: parametro por default
        
        :param i: inicializa un evento
        
        '''
        
        VentanaPrincipal()
        self.Destroy()

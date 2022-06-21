'''
Created on 21 jun 2022

@author: Nico
'''

import wx
import random
import time
from vista.VentanaMensajePerdedor import VentanaMensajePerdedor
from vista.VentanaMensajeGanador import VentanaMensajeGanador


'''

    Esto es un documento
    
'''

'''

    Esto es una clase
    
'''

class VentanaJuego(wx.Dialog):
    
    '''
    
    Encargada de mostrar el tablero y el tiempo del juego

    :param parent: Objeto grafico padre del Dialog
    
    :type parent: wx.Dialog
    
    '''

    def __init__ (self, parent, filas, columnas, tiempo, tipo):
        
        '''
        
        Es el constructor de la clase VentanaJuego.
        
        :param self: parametro por default.
        
        :param parent: objeto grafico del parametro Dialog.
        
        :param filas: insertar numero de filas de la grilla.
        
        :type filas: int
        
        :param columnas: insertar numero de columnas de la grilla.
        
        :type columnas: int
        
        :param tiempo: ingresa el tiempo.
        
        :type tiempo: int
        
        :param tipo: este sirve para elegir el tipo de tiempo.
        
        :type tipo: int
        
        '''
        
        wx.Dialog.__init__(self, parent, wx.NewId(), title = "Memoriza", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        
        
        self.tipo=int(tipo)
        self.panel = wx.Panel(self)
        self.counter = int(tiempo)
        
        self.clicks=0
        self.carta=0
        self.carta2=0
        self.nCarta=""
        self.nCarta2=""
        
        self.contPares=0
        
        self.filas=int(filas)
        self.columnas=int(columnas)
        self.par=int((self.filas*self.columnas)/2)
        
        #Cambiar el color de fondo 
        self.SetBackgroundColour('#B9D9D7')

        #Grilla
        
        #Sizers
        
        self.grillasizer=wx.BoxSizer(wx.VERTICAL)
        self.gridsizer=wx.GridSizer(self.filas, self.columnas,3, 3)
        
        #Labels
        self.lbl1 = wx.StaticText(self, label='Inicio')
        fuente1 = wx.Font(23, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.lbl1.SetFont(fuente1)
        
        self.lbltiempo = wx.StaticText(self, label='TIEMPO RESTANTE')
        fuente2=self.lbltiempo.GetFont()
        fuente2.SetPointSize(15)
        self.lbltiempo.SetFont(fuente2)
        
        #Timer
        if self.tipo==1:
            self.timer = wx.Timer(self)
            self.Bind(wx.EVT_TIMER, self.TerminoReloj, self.timer)
            
        elif self.tipo==2:
            self.timer = wx.Timer(self)
            self.Bind(wx.EVT_TIMER, self.Cronometro,self.timer)
            
        #Randomizador de la grilla
        rdm=random.sample(range(1,20),self.par)
        rdm.extend(rdm)
        random.shuffle(rdm)
        
        #Agregando sizer
        for i in (rdm):
            imagefile=wx.Image("../Cards/back.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
            btn=str(i)
            self.gridsizer.Add(wx.BitmapButton(self,name=btn,bitmap=imagefile, size= (imagefile.GetWidth(), imagefile.GetHeight() )),-1,wx.ALL|wx.ALIGN_CENTER,border=2)
            self.Bind(wx.EVT_BUTTON,self.ContarCartas)
            
        #Configuracion sizer
        self.grillasizer.Add(self.gridsizer, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, border=10)
        self.grillasizer.Add(self.lbltiempo,0, wx.ALIGN_CENTER|wx.ALL, border=0)
        self.grillasizer.Add(self.lbl1, 0, wx.ALIGN_CENTER|wx.ALL, border=0)
        self.SetSizer(self.grillasizer)
        
        #Maximizar la ventana
        self.Maximize(True)
        
        #Se muestra todo a la vez
        self.Show()

    def InicioReloj(self, event=None):
        
        '''
        
        Encargada de inicializar el tiempo una vez se aprete la primera carta.
        
        :param event: inicializa un evento en None de wx.Time.

        :type event: wx.EVT_Timer
        
        '''
        if not self.timer.IsRunning():
            self.timer.Start(1000)

    def TerminoReloj(self, event):
        
        '''
        
        Encargada de ir desminuyendo el contador y posteriormente mostrarlo en pantalla.
        
        :param event: inicializa un evento de wx.Timer.
        
        :type event: wx.EVT_Timer
        
        '''
        if self.counter == -1:
            self.timer.Stop()
            self.Hide()
            ventanaMensaje=VentanaMensajePerdedor(self)
            ventanaMensaje.ShowModal()
            return
        else:
            minutos = self.counter // 60
            segundos = self.counter - (minutos * 60)
            self.counter -= 1

        self.lbl1.SetLabel(f"{str(minutos)}:{str(segundos)}")
        
    def Cronometro(self, event):
        
        '''
        
        Encargada de ir aumentando el contador y posteriormente mostrarlo en pantalla.
        
        :param event: inicializa un evento de wx.Timer.
        
        :type event: wx.EVT_Timer
        
        '''
        
        minutos = self.counter // 60
        segundos = self.counter - (minutos * 60)
        self.counter += 1
        self.lbl1.SetLabel(f"{str(minutos)}:{str(segundos)}")
        
    def CartasTemp(self, event):
        
        '''
        
        Funcion temporal encargada de bloquear que la primera carta no se pueda hacer click dos veces y contar como par.
        
        :param event: inicializa un evento.
        
        '''
        
        pass
        
    def ContarCartas(self, event):
        
        '''
        
        Funcion encargada de verificar si son pares o no, en caso de que sean añadir un contador; ademas se encarga de que la carta se de vuelta una vez se haga click.
        
        :param event: inicializa el evento GetName.
        
        :type event: wx.EVT
        
        '''
        
        self.InicioReloj()
        self.clicks +=1
        
        boton=event.GetEventObject()
        nombreboton=event.GetEventObject().GetName()

        image=wx.Image("../Cards/"+nombreboton+".png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        boton.SetBitmap(image)
        
        if self.clicks==1:
            self.carta=boton
            self.nCarta=nombreboton
            
            self.carta.Bind(wx.EVT_BUTTON,self.CartasTemp)
            
        elif self.clicks==2:
            
            image=wx.Image("../Cards/"+nombreboton+".png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
            boton.SetBitmap(image)
            print("segundacarta")
            if nombreboton == self.nCarta:
                time.sleep(0)
                
                boton.Disable()
                self.carta.Disable()
                boton.SetBitmapDisabled(image)
                self.carta.SetBitmapDisabled(image)
                self.contPares+=1
                self.clicks=0
            elif nombreboton != self.nCarta:
                self.carta2=boton
                self.nCarta2=nombreboton
                self.carta2.Bind(wx.EVT_BUTTON,self.CartasTemp)
        elif self.clicks==3:
            image=wx.Image("../Cards/back.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
            self.carta.SetBitmap(image)
            self.carta.Bind(wx.EVT_BUTTON,self.ContarCartas)
            self.carta2.SetBitmap(image)
            self.carta2.Bind(wx.EVT_BUTTON,self.ContarCartas)
            self.carta=boton
            self.nCarta=nombreboton
            self.clicks=1
        
        if self.contPares==self.par:
            self.timer.Stop()
            self.Hide()
            ventanaMensaje=VentanaMensajeGanador(self)
            ventanaMensaje.ShowModal()
            return 
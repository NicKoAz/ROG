'''
Created on 21 jun 2022

@author: Nico
'''
import wx
from vista.VentanaPrincipal import VentanaPrincipal

if __name__ == "__main__":
    app = wx.App()
    VentanaPrincipal().Show()
    app.MainLoop()
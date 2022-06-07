'''
Created on 16-05-2022

@author: carol
'''

import wx
from source.vista.VentanaPrincipal import VentanaPrincipal

if __name__ == "__main__":
    app = wx.App()
    VentanaPrincipal().Show()
    app.MainLoop()
'''
Created on 07-06-2022

@author: carol
'''


import wx
from vista.VentanaPrincipal import VentanaPrincipal

if __name__ == "__main__":
    app = wx.App()
    VentanaPrincipal().Show()
    app.MainLoop()
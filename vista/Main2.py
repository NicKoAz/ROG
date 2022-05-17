'''
Created on 16-05-2022

@author: carol
'''

import wx
from vista.Interfaz import Interfaz

if __name__ == "__main__":
    app = wx.App()
    Interfaz().Show()
    app.MainLoop()
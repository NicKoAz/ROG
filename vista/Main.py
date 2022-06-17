class Main():
    pass

import wx
from vista.VentanaPrincipal import VentanaPrincipal

if __name__ == "__main__":
    app = wx.App()
    VentanaPrincipal().Show()
    app.MainLoop()
import time
import os
import wx

class ContraReloj(wx.Frame):
    
    def __init__(self):
    
        wx.Frame.__init__(self, None, title='Cronometro')
        panel = wx.Panel(self)
        self.counter = 0

        font = wx.Font(24, wx.FONTFAMILY_ROMAN,
                       wx.FONTSTYLE_NORMAL,
                       wx.FONTWEIGHT_BOLD)

        self.lbl = wx.StaticText(panel, label='Inicio')
        self.lbl.SetFont(font)

        btn = wx.Button(panel, label='Comienza a Contar')
        btn.Bind(wx.EVT_BUTTON, self.start)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.update, self.timer)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.lbl, 0, wx.ALL, 5)
        sizer.Add(btn, 0, wx.ALL|wx.CENTER, 5)
        panel.SetSizer(sizer)

        self.Show()

    def start(self, e):
        self.timer.Start(1000)

    def update(self, e):
        for self.counter in range (0,10):
            for self.contador in range (60):
                os.system ("cls")
                time.sleep(1)
                self.lbl.SetLabel(f" {self.counter}:{self.contador}")
            return

        self.lbl.SetLabel(str(self.counter))


if __name__ == '__main__':
    app = wx.App(False)
    frame = ContraReloj()
    app.MainLoop()
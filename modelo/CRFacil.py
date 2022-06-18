import wx

class ContraReloj(wx.Frame):
    
    def __init__(self):
    
        wx.Frame.__init__(self, None, title='Contra-Reloj')
        panel = wx.Panel(self)
        self.counter = 300

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

    def update(self, event):
        if self.counter == 0:
            self.timer.Stop()
            self.lbl.SetLabel('El juego ha terminado')
            return
        else:
            minutos = self.counter // 60
            segundos = self.counter - (minutos * 60)
            self.counter -= 1

        self.lbl.SetLabel(f"{str(minutos)}:{str(segundos)}")
    
if __name__ == '__main__':
    app = wx.App(False)
    frame = ContraReloj()
    app.MainLoop()
    
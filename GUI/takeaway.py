import wx

class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=1, title='takeaway caculate tool', size=(700, 400), pos=(0, 0))

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(sizer)

        #创建静态文本组件
        txt = wx.StaticText(panel, -1, 'hello')
        sizer.Add(txt, 0, wx.TOP | wx.LEFT, 100)

        # 创建button
        btn = wx.Button(panel, -1, "Quit")
        sizer.Add(btn, 0, wx.TOP|wx.LEFT, 300)
        self.Bind(wx.EVT_BUTTON, self.OnClick, btn)

        # 创建状态栏
        self.CreateStatusBar()
        self.SetStatusText("状态栏信息")

        #将窗口放在桌面环境的中间
        self.Center()


    def OnClick(self, event):
        print("我被点击了")
        self.Close(True)


class MyApp(wx.App):
    def OnInit(self):
        print("开始进入事件循环")
        self.frame = MyFrame(None)
        self.frame.Show(True)
        self.frame.GetId()
        return True

    def OnExit(self):
        print("事件循环结束")
        import time
        time.sleep(2)
        return 0

# app = wx.App()
# frame = MyFrame(None)
# frame.Show(True)
app = MyApp()
app.MainLoop()
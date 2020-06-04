import wx

class MyFrame(wx.Frame):
    def __init__(self, parent=None):
        super(MyFrame, self).__init__(parent, -1, '文本框', size=(600, 300))

        panel = wx.Panel(self, -1)

        Label1 = wx.StaticText(panel, -1, '参与人A: ', pos=(30,10))
        self.inputText = wx.TextCtrl(panel, -1, '', pos=(100, 10), size=(150, -1))
        self.inputText.SetInsertionPoint(0)

        Label2 = wx.StaticText(panel, -1, '参与人B: ', pos=(30, 50))
        self.pwdText = wx.TextCtrl(panel, -1, '', pos=(100, 50), size=(150, -1))

        # Label2 = wx.StaticText(panel, -1, '密码: ', pos=(10, 50))
        # self.pwdText = wx.TextCtrl(panel, -1, '', pos=(80, 50), size=(150, -1), style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER)
        # self.Bind(wx.EVT_TEXT_ENTER, self.OnLostFocus, self.pwdText)

        self.button = wx.Button(panel, -1, "确定", pos=(20, 100))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()
        # self.inputText = wx.TextCtrl(panel, -1, '', pos=(100, 10), size=(150, -1), style=wx.TE_READONLY)

    def OnClick(self):
        self.inputText.Value = "Hello 2"

    def OnLostFocus(self, event):
        wx.MessageBox("%s %s" % (self.inputText.GetValue(), self.pwdText.GetValue()))

app = wx.App()
frame = MyFrame()
frame.Show()

app.MainLoop()
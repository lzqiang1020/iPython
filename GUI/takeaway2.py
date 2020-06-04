import wx

class MyFrame(wx.Frame):
    def __init__(self, parent=None):
        super(MyFrame, self).__init__(parent, -1, '文本框super', size=(600, 300))

        panel = wx.Panel(self, -1)

        label1 = wx.StaticText(panel, -1, '参与人A: ', pos=(30,10))
        self.inputTextLabel1 = wx.TextCtrl(panel, -1, '', pos=(150, 10), size=(150, -1))
        self.inputTextLabel1.SetInsertionPoint(0)
        label1CalResult == wx.StaticText(panel, -1, '')
        sizer.Add(label1CalResult, 0, wx.TOP | wx.LEFT, 100)

        label2 = wx.StaticText(panel, -1, '参与人B: ', pos=(30, 50))
        self.inputTextLabel2 = wx.TextCtrl(panel, -1, '', pos=(150, 50), size=(150, -1))

        label3 = wx.StaticText(panel, -1, '参与人C：', pos=(30, 90))
        self.inputTextLabel3 = wx.TextCtrl(panel, -1, '', pos=(150, 90), size=(150, -1))

        label = wx.StaticText(panel, -1, '实际支付金额：', pos=(30, 130))
        self.inputTextLabel = wx.TextCtrl(panel, -1, '', pos=(150, 130), size=(150, -1))

        self.button = wx.Button(panel, -1, "确定", pos=(20, 200))
        self.Bind(wx.EVT_BUTTON, self.OnClick, self.button)
        self.button.SetDefault()

    def OnClick(self, inputTextLabel1, inputTextLabel2, inputTextLabel):
        print('text abc')
        labelA = self.inputTextLabel1.GetValue()
        labelB = self.inputTextLabel2.GetValue()
        labelC =  self.inputTextLabel3.GetValue()
        label = self.inputTextLabel.GetValue()
        allAmount = labelA + labelB

        discountRate = label / allAmount

        # sizer.Add(txt, 0, wx.TOP | wx.LEFT, 100)
        # return (round(goodsPriceA * discountRate, 2), round(goodsPriceB * discountRate, 2))




app = wx.App()
frame = MyFrame()
frame.Show()

app.MainLoop()

# frame.Bind(wx.EVT_TEXT, frame.OnText, text)
# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 30 2011)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 (wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=u"wxTrainer v0.2b", pos=wx.DefaultPosition, size=wx.Size(400, 250), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHintsSz(wx.Size(400, 200), wx.Size(500, 500))

		gbSizer2 = wx.GridBagSizer(5, 5)
		gbSizer2.AddGrowableCol(0)
		gbSizer2.AddGrowableCol(1)
		gbSizer2.AddGrowableCol(2)
		gbSizer2.AddGrowableCol(3)
		gbSizer2.AddGrowableCol(4)
		gbSizer2.AddGrowableRow(0)
		gbSizer2.AddGrowableRow(1)
		gbSizer2.AddGrowableRow(2)
		gbSizer2.AddGrowableRow(3)
		gbSizer2.AddGrowableRow(4)
		gbSizer2.SetFlexibleDirection(wx.BOTH)
		gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)
		gbSizer2.SetEmptyCellSize(wx.Size(5, 5))

		gbSizer2.SetMinSize(wx.Size(5, 5))
		self.m_staticText5 = wx.StaticText(self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE)
		self.m_staticText5.Wrap(-1)
		self.m_staticText5.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString))

		gbSizer2.Add(self.m_staticText5, wx.GBPosition(0, 0), wx.GBSpan(1, 4), wx.ALIGN_CENTER | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

		self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText6.Wrap(-1)
		gbSizer2.Add(self.m_staticText6, wx.GBPosition(1, 0), wx.GBSpan(1, 2), wx.ALIGN_CENTER | wx.ALL, 5)

		self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText7.Wrap(-1)
		gbSizer2.Add(self.m_staticText7, wx.GBPosition(1, 2), wx.GBSpan(1, 2), wx.ALIGN_CENTER | wx.ALL, 5)

		self.m_button5 = wx.Button(self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
		gbSizer2.Add(self.m_button5, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

		self.m_button6 = wx.Button(self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
		gbSizer2.Add(self.m_button6, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

		self.m_button7 = wx.Button(self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
		gbSizer2.Add(self.m_button7, wx.GBPosition(2, 2), wx.GBSpan(1, 1), wx.ALL, 5)

		self.m_button8 = wx.Button(self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0)
		gbSizer2.Add(self.m_button8, wx.GBPosition(2, 3), wx.GBSpan(1, 1), wx.ALL, 5)

		self.SetSizer(gbSizer2)
		self.Layout()
		self.m_menubar2 = wx.MenuBar(0)
		self.m_menu2 = wx.Menu()
		self.m_menuItem1 = wx.MenuItem(self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL)
		self.m_menu2.AppendItem(self.m_menuItem1)

		self.m_menuItem2 = wx.MenuItem(self.m_menu2, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL)
		self.m_menu2.AppendItem(self.m_menuItem2)

		self.m_menubar2.Append(self.m_menu2, u"MyMenu")

		self.m_menu3 = wx.Menu()
		self.m_menubar2.Append(self.m_menu3, u"MyMenu")

		self.SetMenuBar(self.m_menubar2)

		self.m_statusBar1 = self.CreateStatusBar(1, wx.ST_SIZEGRIP, wx.ID_ANY)

		self.Centre(wx.BOTH)

	def __del__(self):
		pass


###########################################################################
## Class MyFrame2
###########################################################################

class MyFrame2 (wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__ (self, parent, id=wx.ID_ANY, title=u"Config", pos=wx.DefaultPosition, size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
		self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
		self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

		gbSizer3 = wx.GridBagSizer(5, 5)
		gbSizer3.SetFlexibleDirection(wx.BOTH)
		gbSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

		m_radioBox1Choices = [ u"Option 1", u"Option 2", u"Option 3", u"Option 4" ]
		self.m_radioBox1 = wx.RadioBox(self, wx.ID_ANY, u"options", wx.DefaultPosition, wx.Size(150, -1), m_radioBox1Choices, 1, wx.RA_SPECIFY_COLS)
		self.m_radioBox1.SetSelection(3)
		self.m_radioBox1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

		gbSizer3.Add(self.m_radioBox1, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

		m_sdbSizer2 = wx.StdDialogButtonSizer()
		self.m_sdbSizer2OK = wx.Button(self, wx.ID_OK)
		m_sdbSizer2.AddButton(self.m_sdbSizer2OK)
		self.m_sdbSizer2Cancel = wx.Button(self, wx.ID_CANCEL)
		m_sdbSizer2.AddButton(self.m_sdbSizer2Cancel)
		m_sdbSizer2.Realize();
		gbSizer3.Add(m_sdbSizer2, wx.GBPosition(4, 0), wx.GBSpan(1, 4), wx.ALIGN_RIGHT | wx.ALL | wx.EXPAND, 5)

		sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, u"bk"), wx.VERTICAL)

		self.m_textCtrl1 = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_textCtrl1.SetMaxLength(1)
		sbSizer1.Add(self.m_textCtrl1, 0, wx.ALL, 5)

		gbSizer3.Add(sbSizer1, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

		self.SetSizer(gbSizer3)
		self.Layout()

		self.Centre(wx.BOTH)

	def __del__(self):
		pass



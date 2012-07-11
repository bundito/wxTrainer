'''
Created on Jun 20, 2012

@author: sharvey3
'''

import wx

import logging
logging.basicConfig(level = logging.DEBUG)

BTN_HIT = 1000
BTN_STD = 2000
BTN_DBL = 3000
BTN_SPT = 4000
	
class MainFrame(wx.Frame):
	def __init__ (self, parent):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "wxTrainer 0.2b", 
						pos = wx.DefaultPosition, size = wx.Size(400,250), 
						style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		#self.SetSizeHintsSz(wx.Size(400,200), wx.Size(500,500))
		

		
		# Panels
		panel = self.panel = wx.Panel(self)
		panel.SetBackgroundColour(wx.WHITE)
		#panel.SetSizeHintsSz(wx.Size(400,200), wx.Size(500,500))
		
		bpanel = self.bpanel = wx.Panel(self)
		bpanel.Hide()
		
		
		# Menus
		self.m_menubar1 = wx.MenuBar( 0 )
		self.f_menu = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.f_menu, wx.ID_ANY, u"Config", wx.EmptyString, wx.ITEM_NORMAL )
		self.f_menu.AppendItem( self.m_menuItem1 )
		self.m_menubar1.Append( self.f_menu, u"File" ) 
		self.SetMenuBar( self.m_menubar1 )

				
		# Text labels 
		dcard = self.dcard = wx.StaticText(self, -1, "XX", style = wx.ALIGN_CENTER)
		pcard1 = self.pcard1 = wx.StaticText(self, -1, "XX", style = wx.ALIGN_CENTER)
		pcard2 = self.pcard2 = wx.StaticText(self, -1, "XX", style = wx.ALIGN_CENTER)
		
		hit_button = self.hit_button = wx.Button(self, BTN_HIT, "H", wx.DefaultPosition, wx.DefaultSize, 0)
		std_button = self.std_button = wx.Button(self, BTN_STD, "S")
		dbl_button = self.dbl_button = wx.Button(self, BTN_DBL, "D")
		spt_button = self.spt_button = wx.Button(self, BTN_SPT, "P")
		

		# GridBagSizer
		gbs = self.gbs = wx.GridBagSizer(5,5)
		
		# Make all columns & rows growable (stretchable)
#		gbs.AddGrowableCol(0)
#		gbs.AddGrowableCol(1)
#		gbs.AddGrowableCol(2)
#		gbs.AddGrowableCol(3)
#		gbs.AddGrowableCol(4)
#		gbs.AddGrowableRow(0)
#		gbs.AddGrowableRow(1)
#		gbs.AddGrowableRow(2)
#		gbs.AddGrowableRow(3)
#		gbs.AddGrowableRow(4)
		
		# gbs coordinates are row, column
		# spanning value is how many rows and how many columns - 
		# 	NOT a to->from range	
		gbs.Add(dcard, wx.GBPosition(0,0), wx.GBSpan(1,4), flag = wx.ALIGN_CENTER | wx.ALL, border=5)
		gbs.Add(pcard1, wx.GBPosition(1,0), wx.GBSpan(1,2), flag = wx.ALIGN_CENTER | wx.ALL, border=5)
		gbs.Add(pcard2, wx.GBPosition(1,2), wx.GBSpan(1,2), flag = wx.ALIGN_CENTER | wx.ALL, border=5)
		
		gbs.Add(hit_button, wx.GBPosition(2,0), wx.GBSpan(1,1), wx.ALL, 5)
		gbs.Add(std_button, wx.GBPosition(2,1), wx.GBSpan(1,1), wx.ALL, 5)
		gbs.Add(dbl_button, wx.GBPosition(2,2), wx.GBSpan(1,1), wx.ALL, 5)
		gbs.Add(spt_button, wx.GBPosition(2,3), wx.GBSpan(1,1), wx.ALL, 5)
#		
#		button_box = wx.BoxSizer()
#		button_box.SetMinSize(wx.Size(400,100))
#				
#		button_box.Add(hit_button, 1)
#		button_box.Add(std_button, 1)
#		button_box.Add(dbl_button, 1)
#		button_box.Add(spt_button, 0)
#		
#		gbs.Add(button_box, (3,0), (1,2), flag = wx.ALIGN_CENTER, border = 5)

		gbs.AddGrowableCol(0)
		gbs.AddGrowableCol(1)
		gbs.AddGrowableCol(2)
		gbs.AddGrowableCol(3)
##		gbs.AddGrowableCol(4)
		gbs.AddGrowableRow(0)
		gbs.AddGrowableRow(1)
		gbs.AddGrowableRow(2)
#		gbs.AddGrowableRow(3)
##		gbs.AddGrowableRow(4)

		#box = wx.BoxSizer()
		#box.Add(gbs, 1, wx.ALL, 10)
			
		#panel.Layout()
			
		self.SetSizerAndFit(gbs)
		#panel.SetSize(gbs.GetSize())

#		panel.SetSizer(gbs)
#		panel.Layout()
#		
		# For now, use the size of the box and not the box itself
		# (perhaps there's an issue with reusing a sizer?)
#		bpanel.SetSize(box.GetSize())
#		
#		self.SetClientSize(panel.GetSize())
		
				# Keyboard binding
		self.Bind(wx.EVT_CHAR_HOOK, self.keypress)
		
		# Button bindings
		self.Bind(wx.EVT_BUTTON, self.OnButton, hit_button)
		self.Bind(wx.EVT_BUTTON, self.OnButton, std_button)
		self.Bind(wx.EVT_BUTTON, self.OnButton, dbl_button)
		self.Bind(wx.EVT_BUTTON, self.OnButton, spt_button)
		
		def OnButton(self, event):
			event.Skip()
		
		def OnKey(self, event):
			event.Skip()
			


class TestDialog(wx.Dialog):
	def __init__(self, parent, id = wx.ID_ANY, title = "Test", size=wx.DefaultSize, pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE, useMetal=False):
		super (TestDialog, self).__init__(parent, id, title, pos, size, style)
		
		type = "Spam spam spam"
		
		self.type = wx.TextCtrl(self, value=type, style=wx.TE_READONLY)
		self.details = wx.TextCtrl(self, value="", style=wx.TE_READONLY | wx.TE_MULTILINE)
		# Layout
		self.__DoLayout()
		self.SetInitialSize()

	def __DoLayout(self):
		sizer = wx.GridBagSizer(vgap=8, hgap=8)
		type_lbl = wx.StaticText(self, label="Type:")
		detail_lbl = wx.StaticText(self, label="Details:")
		# Add the event type fields
		sizer.Add(type_lbl, (1, 1))
		sizer.Add(self.type, (1, 2), (1, 15), wx.EXPAND)
		# Add the details field
		sizer.Add(detail_lbl, (2, 1))
		sizer.Add(self.details, (2, 2), (5, 15), wx.EXPAND)
		# Add a spacer to pad out the right side
		sizer.Add((5, 5), (2, 17))
		# And another to the pad out the bottom
		sizer.Add((5, 5), (7, 0))
		self.SetSizer(sizer)
			
	
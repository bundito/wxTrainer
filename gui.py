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
	def __init__ (self, parent, id = wx.ID_ANY, title = "Trainer",
					pos=wx.DefaultPosition, size=wx.DefaultSize,
					style=wx.DEFAULT_FRAME_STYLE, name = "My Frame"):
		
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 620,406 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
#		super (MainFrame, self).__init__(parent, id, title, pos, size, style, name)
		
		
		# Attributes
		panel = self.panel = wx.Panel(self)
		panel.SetBackgroundColour(wx.WHITE)
		
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.f_menu = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.f_menu, wx.ID_ANY, u"Config", wx.EmptyString, wx.ITEM_NORMAL )
		self.f_menu.AppendItem( self.m_menuItem1 )
		
		self.m_menubar1.Append( self.f_menu, u"File" ) 
		
		self.SetMenuBar( self.m_menubar1 )

		# Attempt to hack up a gridbagsizer
		gbs = self.gbs = wx.GridBagSizer(5,5)
				
		# downcard = self.downcard = wx.StaticText(panel, -1, "XX")
		dcard = self.dcard = wx.StaticText(panel, -1, "XX")
		pcard1 = self.pcard1 = wx.StaticText(panel, -1, "XX")
		pcard2 = self.pcard2 = wx.StaticText(panel, -1, "XX")
		
		hit_button = self.hit_button = wx.Button(panel, BTN_HIT, "H")
		std_button = self.std_button = wx.Button(panel, BTN_STD, "S")
		dbl_button = self.dbl_button = wx.Button(panel, BTN_DBL, "D")
		spt_button = self.spt_button = wx.Button(panel, BTN_SPT, "P")
		
		
		# gbs coordinates are row, column
		# spanning value is how many rows and how many columns - 
		# 	NOT a to->from range
		
		gbs.Add(dcard, (0,0), (1,2), flag = wx.ALIGN_CENTER, border=5)
		#gbs.Add(downcard, (0,1))
		gbs.Add(pcard1, (1,0), flag = wx.ALIGN_CENTER)
		gbs.Add(pcard2, (1,1), flag = wx.ALIGN_CENTER)
		
		gbs.Add(hit_button, (2,0))
		gbs.Add(std_button, (2,1))
		gbs.Add(dbl_button, (3,0))
		gbs.Add(spt_button, (3,1))
		
		
		
		box = wx.BoxSizer()
		box.Add(gbs, 0, wx.ALL, 10)
		
		panel.SetSizerAndFit(box)
		self.SetClientSize(panel.GetSize())
		
		
		
		panel.SetFocus()

		logging.debug("Frame is top level? %s" % self.IsTopLevel())
#		
		
		# Keyboard binding
		self.Bind(wx.EVT_CHAR_HOOK, self.keypress)
		
		# Button bindings
		self.Bind(wx.EVT_BUTTON, self.OnButton, hit_button)
		self.Bind(wx.EVT_BUTTON, self.OnButton, std_button)
		self.Bind(wx.EVT_BUTTON, self.OnButton, dbl_button)
		self.Bind(wx.EVT_BUTTON, self.OnButton, spt_button)
		
		def OnButton(self, event):
			event.Skip()
		
		def OnHit(self, event):
			logging.debug("OnHit in gui")
			event.Skip()
			
		def OnStand(self, event):
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
			
	
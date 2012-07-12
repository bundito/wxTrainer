'''
Created on Jun 20, 2012

@author: sharvey3
'''

import wx
import wx.grid as gridlib

import logging



# Global vars for button ID's (still useful?)
BTN_HIT = 1000
BTN_STD = 2000
BTN_DBL = 3000
BTN_SPT = 4000
	
class MainFrame(wx.Frame):
	def __init__ (self, parent):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "wxTrainer 0.2b", 
						pos = wx.DefaultPosition, size = wx.Size(450,550), 
						style = (wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL) ^ (wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
		
		#=======================================================================
		# Make some panels
		#=======================================================================
		
		# Main panel		
		panel = self.panel = wx.Panel(self)
		panel.SetBackgroundColour(wx.WHITE)
		
		# Boss panel - in it's own class so it can be customized
		bpanel = self.bpanel = BossPanel(self)
		self.bpanel.Hide()

		
		# Menus
		self.m_menubar1 = wx.MenuBar( 0 )
		self.f_menu = wx.Menu()
		self.m_menuItem1 = wx.MenuItem( self.f_menu, wx.ID_ANY, u"Config", wx.EmptyString, wx.ITEM_NORMAL )
		self.f_menu.AppendItem( self.m_menuItem1 )
		self.m_menubar1.Append( self.f_menu, u"File" ) 
		self.SetMenuBar( self.m_menubar1 )

		#=======================================================================
		# Add stuff to main panel
		#=======================================================================
				
		# Text labels 
		dcard = self.dcard = wx.StaticText(panel, -1, "XX", style = wx.ALIGN_CENTER)
		pcard1 = self.pcard1 = wx.StaticText(panel, -1, "XX", style = wx.ALIGN_CENTER)
		pcard2 = self.pcard2 = wx.StaticText(panel, -1, "XX", style = wx.ALIGN_CENTER)
		
		# Buttons
		hit_button = self.hit_button = wx.Button(panel, BTN_HIT, "H", wx.DefaultPosition, wx.DefaultSize, 0)
		std_button = self.std_button = wx.Button(panel, BTN_STD, "S")
		dbl_button = self.dbl_button = wx.Button(panel, BTN_DBL, "D")
		spt_button = self.spt_button = wx.Button(panel, BTN_SPT, "P")
		

		#=======================================================================
		# Build GridBagSizer for tidy layout
		#=======================================================================

		# GridBagSizer
		gbs = self.gbs = wx.GridBagSizer(5,5)
		
		# gbs coords are row, column - span is rowspan & colspan, not to/from 	
		gbs.Add(dcard, wx.GBPosition(0,0), wx.GBSpan(1,4), flag = wx.ALIGN_CENTER | wx.ALL, border=5)
		gbs.Add(pcard1, wx.GBPosition(1,0), wx.GBSpan(1,2), flag = wx.ALIGN_CENTER | wx.ALL, border=5)
		gbs.Add(pcard2, wx.GBPosition(1,2), wx.GBSpan(1,2), flag = wx.ALIGN_CENTER | wx.ALL, border=5)
		
		gbs.Add(hit_button, wx.GBPosition(2,0), wx.GBSpan(1,1), wx.ALL, 5)
		gbs.Add(std_button, wx.GBPosition(2,1), wx.GBSpan(1,1), wx.ALL, 5)
		gbs.Add(dbl_button, wx.GBPosition(2,2), wx.GBSpan(1,1), wx.ALL, 5)
		gbs.Add(spt_button, wx.GBPosition(2,3), wx.GBSpan(1,1), wx.ALL, 5)
			
		#=======================================================================
		#  Finalize layout, set panel & frame sizes
		#=======================================================================

		# Stuff everything into a nice, tidy box
		box = wx.BoxSizer()
		box.Add(gbs, 1, wx.ALL, 10)
		
		# Assign the box to the panel
		panel.SetSizerAndFit(box)
			
		# Use the box's size to size the second panel
		bpanel.SetSize(box.GetSize())
		
		# Set the parent wx.Frame to be the same size as the panel
		self.SetClientSize(panel.GetSize())
		
				
		#===============================================================================
		# Event bindings...
		#===============================================================================
				
		# Keyboard
		self.Bind(wx.EVT_CHAR_HOOK, self.keypress)
		
		# Buttons
		self.Bind(wx.EVT_BUTTON, self.OnButton, hit_button)
		self.Bind(wx.EVT_BUTTON, self.OnButton, std_button)
		self.Bind(wx.EVT_BUTTON, self.OnButton, dbl_button)
		self.Bind(wx.EVT_BUTTON, self.OnButton, spt_button)
		
		
		#=======================================================================
		# Event handlers (currently [7/12] outsourced to mainapp.py)
		#=======================================================================
		
		def OnButton(self, event):
			event.Skip()
		
		def OnKey(self, event):
			event.Skip()
	
	
	#===========================================================================
	# Object methods belong at THIS outdent level 
	#===========================================================================
			
	def SwapView(self):
		logging.info("Swapping...")
		
		bsize = wx.Size(700,400)
		origsize = wx.Size(450,300)
		
		if self.panel.IsShown():
			self.panel.Hide()
			self.bpanel.SetSize(bsize)
			self.bpanel.Show()
			self.SetSize(bsize)
		else:
			self.panel.Show()
			self.panel.SetSize(origsize)
			self.SetSize(origsize)
			self.bpanel.Hide()
		


#===============================================================================
# BossPanel class - subclasses Panel, separated for ease of customizing
#===============================================================================

class BossPanel(wx.Panel):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        wx.Panel.__init__(self, parent=parent)
 
        grid = gridlib.Grid(self)
        grid.CreateGrid(25,12)
 
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(grid, 0, wx.EXPAND)
        self.SetSizer(sizer)




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
			
	
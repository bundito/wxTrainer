'''
Created on Jun 20, 2012

@author: sharvey3
'''

import wx
import wx.grid as gridlib

import config
from config import options

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

		# Configuration dialog
		cfg_dialog = self.cfg_dialog = ConfigDialog(self)
		
		# Menus
		self.mb = wx.MenuBar(0)
		
		# File Menu & Items
		self.filemenu = wx.Menu()
		self.mi_config = wx.MenuItem(self.filemenu, wx.ID_ANY, u"Config", wx.EmptyString, wx.ITEM_NORMAL)
		self.filemenu.AppendItem(self.mi_config)
		
		# Build menu
		self.mb.Append(self.filemenu, u"File") 
		self.SetMenuBar(self.mb)

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
		self.Bind(wx.EVT_CHAR_HOOK, self.OnKey)
		
		# Buttons
		self.Bind(wx.EVT_BUTTON, self.OnButton, hit_button)
		self.Bind(wx.EVT_BUTTON, self.OnButton, std_button)
		self.Bind(wx.EVT_BUTTON, self.OnButton, dbl_button)
		self.Bind(wx.EVT_BUTTON, self.OnButton, spt_button)
		
		# Menus
		self.Bind(wx.EVT_MENU, self.DoConfig, self.mi_config)
		
		#=======================================================================
		# Button & Key handlers (currently [7/12] outsourced to mainapp.py)
		#=======================================================================
		
		def OnButton(self, event):
			event.Skip()
		
		def OnKey(self, event):
			event.Skip()
	
		def DoConfig(self, event):
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
			self.bpanel.SetFocus()
		else:
			self.panel.Show()
			self.panel.SetSize(origsize)
			self.SetSize(origsize)
			self.bpanel.Hide()
			self.panel.SetFocus()
		


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


#===============================================================================
# Config dialog
#===============================================================================


class ConfigDialog(wx.Dialog):
	def __init__(self, parent, id = wx.ID_ANY, title = "Options", size=wx.DefaultSize, 
				pos=wx.DefaultPosition, style=wx.DEFAULT_DIALOG_STYLE, useMetal=False):
		super (ConfigDialog, self).__init__(parent, id, title, pos, size, style)
		
		panel = wx.Panel(self)
		
		#=======================================================================
		# Config (main) items...
		#=======================================================================
	
		ht_pref = options.get('main-opts', 'htype')	
		ht_choices = ["A - xxxxx", "H - xxxxx", "S - xxxx", "D - xxxxx", "P - xxxxx"]
		ht_box = self.ht_box = wx.RadioBox(panel, -1, "HT", choices = ht_choices, majorDimension = 1)
		ht_box.SetStringSelection(ht_pref)
		
		view_choices = ['Txt', 'Gfx']
		view_box = self.view_box = wx.RadioBox(panel, -1, "View", choices = view_choices, majorDimension = 1)
		view_box.SetStringSelection(options.get('main-opts', 'view'))
		
		bkey_label = wx.StaticText(panel, -1, "Bkey")		
		bkey_pref = options.get('main-opts', 'bkey')
		bkey_choice = self.bkey_choice = wx.TextCtrl(panel, -1, bkey_pref, size=(125, -1))
		
		btype_label = wx.StaticText(panel, -1, "BK Type")
		btype_choices = ['Grid', 'Image', 'Hide']
		btype_picker = self.btype_picker = wx.Choice(panel, -1, choices = btype_choices)
		btype_picker.SetStringSelection(options.get('main-opts', 'bk_type'))
		
		disable_pref = options.getboolean('main-opts', 'btn_disable')
		logging.info(disable_pref)
		btn_disable = self.btn_disable = wx.CheckBox(panel, -1, "Disable Invalid Buttons")
		btn_disable.SetValue(disable_pref)
		btn_hint = wx.StaticText(panel, -1, "Lorem ipsum dolor sit amet amet lorem ipsum dolor sit ametamet lorem ipsum dolor sit amet.")
		btn_hint.Wrap(150)
	
		
	
		#=======================================================================
		# Create GBS, add items
		#=======================================================================
		
		cfg_gbs = wx.GridBagSizer(5,5)
		
		cfg_gbs.Add(ht_box, (0,0), (3,2), wx.ALL|wx.EXPAND|wx.ALIGN_CENTER, 5)
		cfg_gbs.Add(view_box, (0,2), (3, 2), wx.ALL|wx.EXPAND|wx.CENTER, 5)
		
		cfg_gbs.Add(bkey_label, (3, 2))
		cfg_gbs.Add(bkey_choice, (3, 3))
		
		cfg_gbs.Add(btype_label, (4,2))
		cfg_gbs.Add(btype_picker, (4,3))
		
		cfg_gbs.Add(btn_disable, (4,0), (1, 2), wx.EXPAND|wx.ALL, 5)
		cfg_gbs.Add(btn_hint, (6,0), (2,2), wx.EXPAND|wx.ALL, 5)
		
		
#		Add standard OK/Cancel buttons using Standard Dialog Button sizer
		sdbs = wx.StdDialogButtonSizer()
		ok_button = wx.Button(panel, wx.ID_OK)
		cancel_button = wx.Button(panel, wx.ID_CANCEL)
		
		sdbs.AddButton(ok_button)
		sdbs.AddButton(cancel_button)
		sdbs.Realize()
		
#		Add dialog button set to bottom of GBS
		cfg_gbs.Add(sdbs, (8,1), (1,4), wx.ALIGN_RIGHT | wx.EXPAND | wx.ALL , 5)
		
		panel.SetSizerAndFit(cfg_gbs)
		self.SetClientSize(panel.GetSize())
	
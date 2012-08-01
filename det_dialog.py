'''
Created on Jul 2, 2012

@author: sharvey3
'''

import wx

class DetailsDialog(wx.Dialog):
	def __init__(self, parent):
		"""Create the dialog
		@param type: event type string
		@param details: long details string
		"""
		super(DetailsDialog, self).__init__(self, parent)

		# Attributes
		self.type = wx.TextCtrl(self, value=type,
		style=wx.TE_READONLY)
		self.details = wx.TextCtrl(self, value="",
		style=wx.TE_READONLY |
		wx.TE_MULTILINE)
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

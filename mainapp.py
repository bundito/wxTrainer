'''
Created on Jun 27, 2012

@author: sharvey3
'''
import wx
import gui
import cards
import strategy
import config
from config import options

import logging
logging.basicConfig(level = logging.INFO)

logging.info("htype read as %s" % options.get('main-opts', 'htype'))

# Yeah... this sucks. There must be a better way of handling buttons
play_ids = dict({1000: "H", 2000: "S", 3000: "D", 4000: "S"})


chart = strategy.table()

class mf(gui.MainFrame):
	def __init__(self, parent ):
		gui.MainFrame.__init__(self, parent )
		
		logging.debug("mf initialized")
			
		self.deal()
		
	def OnButton(self, event):
		self.CheckPlay(play_ids[event.Id])
		
	def DoConfig(self, event):
		dlg = self.cfg_dialog
		retval = dlg.ShowModal()
		
		if retval == wx.ID_OK:
			logging.info("Ok")
			options.set('main-opts', 'htype', dlg.ht_box.StringSelection)
			options.set('main-opts', 'view', dlg.view_box.StringSelection)
			options.set('main-opts', 'bkey', dlg.bkey_choice.Value)
			options.set('main-opts', 'bk_type', dlg.btype_picker.StringSelection)
			btn_disable = dlg.btn_disable.IsChecked()
			options.set('main-opts', 'btn_disable', str(dlg.btn_disable.IsChecked()))
			
			config.save_options()
		
		elif retval == wx.ID_CANCEL:
			logging.info("Cancelled.")

	def OnKey(self, event):
		logging.debug("OnKey triggered in mainapp")
		keycode = event.GetKeyCode()
		if keycode <= 256:
			key = chr(keycode)
			
			if key != "Q":
				self.CheckPlay(key)
			else:
				self.SwapView()

	def deal(self):
		h = cards.playerhand()
		d = cards.dealercard()
		c1 = h.c1.display
		c2 = h.c2.display
		
		self.correct = chart.get_correct(h.lookup, d.value)
		
		logging.debug("%s %s" % (c1, c2))
		
		self.dcard.SetLabel(d.display)
		self.pcard1.SetLabel(c1)
		self.pcard2.SetLabel(c2)
		
		
	def CheckPlay(self, play):
		logging.info("Button: %s" % play)
		if play == self.correct:
			print "Right."
		else:
			print "Wrong."
		
		self.deal()



class MyApp(wx.App):
	def OnInit(self):
		self.frame = mf(None)
		self.SetTopWindow(self.frame)
		self.frame.Show()
		
		return True
	
	
if __name__ == "__main__":
	app = MyApp(False)
	app.MainLoop()
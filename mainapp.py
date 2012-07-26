'''
Created on Jun 27, 2012

@author: sharvey3
'''
import wx
import random
import gui
import cards
import strategy
import config
from config import options

import logging
logging.basicConfig(level = logging.INFO)

htype = options.get('main-opts', 'htype')

# Yeah... this sucks. There must be a better way of handling buttons
play_ids = dict({1000: "H", 2000: "S", 3000: "D", 4000: "S"})

# More temporary ugliness...
htypes = dict({'A - xxxxx': 'all', 'H - xxxxx': 'hard', 'S - xxxxx' : 'soft', 'P - xxxxx': 'split'})

chart = strategy.table()

class mf(gui.MainFrame):
	def __init__(self, parent ):
		gui.MainFrame.__init__(self, parent )
			
		self.handtype = htypes[htype]	
		self.deal()
	
	
		
	def OnButton(self, event):
		self.CheckPlay(play_ids[event.Id])
		
	def DoConfig(self, event):
		dlg = self.cfg_dialog
		retval = dlg.ShowModal()
		
		if retval == wx.ID_OK:					
			options.set('main-opts', 'htype', dlg.ht_box.StringSelection)
			options.set('main-opts', 'view', dlg.view_box.StringSelection)
			options.set('main-opts', 'bkey', dlg.bkey_choice.Value)
			options.set('main-opts', 'bk_type', dlg.btype_picker.StringSelection)
			btn_disable = dlg.btn_disable.IsChecked()
			options.set('main-opts', 'btn_disable', str(dlg.btn_disable.IsChecked()))
			
			config.save_options()
			
			self.handtype = htypes[dlg.ht_box.StringSelection]
			self.ButtonDisable(0)
			self.deal()
		
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
#		logging.info('deal() thinks handtype is %s' % self.handtype)

		self.handtype = htypes[htype]

		if self.handtype == "all":
			types = ('soft', 'hard', 'split')
			self.handtype = random.choice(types)		
		
#			logging.debug("Hand: %s" % handtype)


		h = cards.playerhand(self.handtype)
		d = cards.dealercard()
		c1 = h.c1.display
		c2 = h.c2.display
		
		logging.info("Value is %s" % h.lookup)
		
		self.correct = chart.get_correct(h.lookup, d.value)
		
		logging.debug("%s %s" % (c1, c2))
		
		self.dcard.SetLabel(d.display)
		self.pcard1.SetLabel(c1)
		self.pcard2.SetLabel(c2)
		
		if options.getboolean('main-opts', 'btn_disable'):
			self.ButtonDisable(h.lookup)	
		

		
	def CheckPlay(self, play):
		logging.info("Button: %s" % play)
		if play == self.correct:
			logging.info("Right.")
		else:
			logging.info("Wrong.")
		
		self.deal()

		
		
	def ButtonDisable(self, value):
		
		self.spt_button.Enable()
		self.dbl_button.Enable()
		
		if self.handtype == "hard":
			self.spt_button.Disable()
			
			if value not in ('8', '9','10', '11'):
				self.dbl_button.Disable()
			else:
				self.dbl_button.Enable()
			
			return
				
		elif self.handtype == "soft":
			self.spt_button.Disable()
			
		
		


class MyApp(wx.App):
	def OnInit(self):
		self.frame = mf(None)
		self.SetTopWindow(self.frame)
		self.frame.Show()
		
		return True
	
	
if __name__ == "__main__":
	app = MyApp(False)
	app.MainLoop()
'''
Created on Jun 18, 2012
	Reads the YML strategy table
@author: sharvey3

'''		
import re
import yaml

class table():

	plays = ({})

	def __init__(self):
		'''
		'''
		
		stream = file('table.yml', 'r')
		table = yaml.load(stream)
		stream.close()
		
		d_cards = re.split(' ', "2 3 4 5 6 7 8 9 10 A")
		
		for p_hand in table.keys():
				
			p_plays = re.split(' *', table[p_hand])
		
			i = 0
		
			for d_has in d_cards:
				p_play = p_plays[i]
				self.plays[str(p_hand), str(d_has)] = p_play
				i += 1
		
			
	def get_correct(self, phand, dcard, simple = True):
		
		lookup = self.plays[phand, dcard]
		
		if simple:
			if lookup == "DH":
				lookup = "D"
			elif lookup == "RH":
				lookup = "H"
			elif lookup == "DS":
				lookup = "D"
			elif lookup == "RS":
				lookup = "S"
			elif lookup == "PH":
				lookup = "P"
			
		
		return lookup	

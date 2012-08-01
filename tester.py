'''
Created on Jun 19, 2012

@author: sharvey3
'''
import cards
import strategy

chart = strategy.table()

for i in range(1, 200):

	h = cards.playerhand()
	d = cards.dealercard()
	correct = chart.get_correct(h.lookup, d.value)

	print "XX", d.display
	print h.display
	#print h.lookup
	print correct
	print "---"
	#print


	i += 1

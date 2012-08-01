'''
Created on Jun 13, 2012

@author: sharvey3
'''

import cards
import strategy

chart = strategy.table()

player_input = ""

while player_input != "Q":

	h = cards.playerhand()
	d = cards.dealercard()
	correct = chart.get_correct(h.lookup, d.value)

	print "XX", d.display
	print h.display
	# print correct

	player_input = raw_input("H S P D (Q)? ")
	player_input = player_input.upper()

	if player_input == correct:
		print "Correct!"
	elif player_input == "Q":
		print "Thanks for your time."
		break
	else:
		print "Sorry - correct answer is", correct

	print










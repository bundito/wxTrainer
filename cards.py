'''
Created on Jun 14, 2012
    Generates cards and player hands
@author: sharvey3
'''
import random
import logging


# Let's define a few globals to make life easier...

SOFT = 1
NO_ACE = 2
NO_5_10 = 3

class newcard():
    '''
    Randomly generate a card
    '''

    random.seed()

    def __init__(self, labeltype="all"):
        '''
        Constructor
        '''

        labels = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

        if labeltype == SOFT:
            labels = ('2', '3', '4', '5', '6', '7', '8', '9')

        elif labeltype == NO_5_10:
            labels = ('2', '3', '4', '6', '7', '8', '9', 'A')

        elif labeltype == NO_ACE:
            labels = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

        elif len(labeltype) == 1:
            labels = labeltype

        # Suit doesn't matter as there are multiple cards in a shoe
        # Also pick a random label
        self.suit = random.choice('CHSD')
        self.label = random.choice(labels)

        # Convert 10, J, Q, K (strings in labels set) to numeric 10
        if self.label in ('10', 'J', 'Q', 'K'):
            self.value = 10
        else:
            self.value = self.label

        self.display = self.label + self.suit


# ----------------------------------


class playerhand():
    '''
    Generate a player's hand from 2 cards
    '''

    def __init__(self, handtype):

        tests = 0

        if handtype == "soft":
            c1 = self.c1 = newcard("A")
            c2 = self.c2 = newcard(SOFT)

        elif handtype == "hard":
            c1 = self.c1 = newcard(NO_ACE)
            c2 = self.c2 = newcard(NO_ACE)

            while c2.value == c1.value:
                c2 = self.c2 = newcard(NO_ACE)
                tests += 1

        elif handtype == "split":
            c1 = self.c1 = newcard(NO_5_10)
            c2 = self.c2 = newcard(NO_5_10)

            if c2.value != c1.value:
                c2 = self.c2 = newcard(c1.label)
                tests += 1

        logging.debug("Tests: %i" % tests)

        # Compile the hand's "lookup" value to match the keys found
        # in the YAML strategy table (15, A4, 77, etc.)
        if c1.value == c2.value:
            self.lookup = str(c1.value) + str(c2.value)
        elif c1.value == 'A':
            self.lookup = 'A' + str(c2.value)
        else:
            self.lookup = int(c1.value) + int(c2.value)

        self.lookup = str(self.lookup)
        # And, at long last, a nicely printable version of your hand
        self.display = c1.display + " " + c2.display






# ---------------------------

class dealercard(newcard):
    '''
    Simple: get a card for the dealer
    '''

    def __init__(self):
        dcard = newcard()
        self.value = str(dcard.value)
        self.display = dcard.display



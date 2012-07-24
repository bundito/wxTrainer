import ConfigParser
import logging

CFG_FILE = './wxTrainer.cfg'
CFG_SECTION = 'main-opts'

options = ConfigParser.SafeConfigParser()
options.read(CFG_FILE)



#===============================================================================
# Convenience functions
#===============================================================================

def save_options():
	with open(CFG_FILE, 'wb') as cfile:
		options.write(cfile)


def set_option(option, value):
	options.set(CFG_SECTION, option, value)
	


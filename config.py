import ConfigParser
import logging

CFG_FILE = './wxTrainer.cfg'
CFG_SECTION = 'sample-cfg'

#===============================================================================
# Convenience functions
#===============================================================================

def save_optns():
	with open(CFG_FILE, 'wb') as cfile:
		cp.write(cfile)

def set_option(option, value):
	cp.set(CFG_SECTION, option, value)


cp = ConfigParser.SafeConfigParser()
cp.read(CFG_FILE)

options = cp.items(CFG_SECTION)

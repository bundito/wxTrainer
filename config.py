import ConfigParser
import logging

CFG_FILE = './wxTrainer.cfg'

config = ConfigParser.ConfigParser()
message = "No config set yet."

def read_cfg():
	config.read(CFG_FILE)
	message = config.get('sample-cfg', 'message')

def add_cfg(text):
	logging.info(text)
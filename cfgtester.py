import config
from config import options

#print options

# options.set('main-opts', 'htype', 'spam')

#
#config.save_options()

htype = options.get('main-opts', 'htype')
print htype

#import logging
#logging.basicConfig(level = logging.INFO)
#
#opts = cfg.options
#print opts
#
#cfg.set_option('message', 'eggs')
#
#opts = cfg.options
#
#print opts

#print cfg.opts_dict['message']
#print cfg.opts_dict['htype']
#
#cfg.opts_dict['message'] = "Spam"
#
#print cfg.opts_dict['message']
#
#print cfg.opts_dict

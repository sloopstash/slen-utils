# -*- coding: utf-8 -*-
from __future__ import (absolute_import,unicode_literals)

# Import community modules.
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('/etc/slen/main.ini')
config = {
  'system':{
    'base_home_dir':parser.get('system','base_home_dir')
  },
  'account':{
    'full_domain':parser.get('account','full_domain'),
    'scheme':parser.get('account','scheme')
  },
  'user':{
    'api_key_identifier':parser.get('user','api_key_identifier'),
    'api_key_token':parser.get('user','api_key_token')
  }
}

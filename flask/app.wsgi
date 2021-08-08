import sys
sys.path.insert(0, '/usr/local/lib/python3.8/site-packeages')
sys.path.insert(0, '/home/ipocc/flask')

import os

os.chdir(os.path.dirname(__file__))

from flask import app as application
import os
import sys

# For future me, the site was at least live by 2018-12-14

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(basedir)


import rrprojects

application = rrprojects.application

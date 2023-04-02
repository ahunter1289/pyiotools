# Scantree test
# Author: Andy Hunter

# Initial import
import sys
import os

# Path config
pyiotools_dir = os.getcwd()[0:-6]
if pyiotools_dir not in sys.path:
    sys.path.append(pyiotools_dir)

# Import pyiotools
from pyiotools import tools as tl
from pyiotools import utils as ut
from pyiotools.imp import *

# Clean workspace
#plt.close('all')
#ut.clear_var()
#ut.clear_console()

# Analysis
[dirslist, fileslist, symlinklist] = tl.scan_tree(pyiotools_dir)

test1 = '/Users/andrewhunter/offlinedocs/swdev/pyiotoolsproject/docs'
test2 = '/Users/andrewhunter/offlinedocs/swdev/pyiotoolsproject/pyiotools'
test3 = '/Users/andrewhunter/offlinedocs/swdev/pyiotoolsproject/environment.yml'
test4 = '/Users/andrewhunter/offlinedocs/swdev/pyiotoolsproject/tests/run_test_template.py'

if test1 in dirslist and test2 in dirslist:
    print('scan tree test passed')
else:
    raise Exception('scan tree test failed')
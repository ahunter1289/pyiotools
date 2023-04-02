# CSV test
# Author: Andy Hunter

# Initial import
import sys
import os

# Path config
pyiotools_dir = os.getcwd()
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
csv1 = tl.import_csv('/Users/andrewhunter/offlinedocs/swdev/pyiotoolsproject/data/csvtest.csv')
csv2 = tl.import_csv('/Users/andrewhunter/offlinedocs/swdev/pyiotoolsproject/data/csvtest_2.csv')
if not csv1[0][0]=='header1' or not csv1[0][3]=='header4' or not csv1[1][0]=='1' or not csv1[1][3]=='4':
    raise Exception('csv test failed')
else:
    print('csv test passed')
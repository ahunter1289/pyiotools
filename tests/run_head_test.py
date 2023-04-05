# Head test
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
#ut.clear_console()
#ut.clear_var()

# Analysis

data = tl.import_csv(os.getcwd()[0:-6]+ '/data/csvtest_3.csv')
search_val = np.array(['header1'])
first_row = tl.data_by_row_name(data,search_val)
search_val = ['header5']
last_row = tl.data_by_row_name(data,search_val,return_cols=2)

data2 = tl.import_csv(os.getcwd()[0:-6]+ '/data/csvtest_2.csv')
search_val2 = np.array(['header4'])
col = tl.data_by_col_name(data2,search_val2,return_rows=3)

if len(last_row[0])==2 and last_row[0][1]=='14' and first_row[0][1]=='2' and col[0][2]=='12' and len(last_row)==2:
    print('head test passed')
else:
    raise Exception('head test failed')




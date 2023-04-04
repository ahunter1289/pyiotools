# Run all tests
# Author: Andy Hunter

# Initial import
import sys
import os

# Path config
pyiotools_dir = os.getcwd()[0:-6]
if pyiotools_dir not in sys.path:
    sys.path.append(pyiotools_dir)
pyiotools_test_dir = os.getcwd()
if pyiotools_test_dir not in sys.path:
    sys.path.append(pyiotools_dir)

# Import pyiotools
from pyiotools import tools as tl
from pyiotools import utils as ut
from pyiotools.imp import *

# Clean workspace
plt.close('all')
ut.clear_console()
ut.clear_var()

# Analysis

import run_beam_test
import run_csv_test
import run_scan_tree_test
import run_head_test
import run_image_test
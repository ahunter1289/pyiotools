# Beam test
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
img_file = os.path.join(os.getcwd()[0:-6], 'data','airydisk-rings.jpg')
ffimage = tl.FarFieldGaussImage(img_file)
centroid = ffimage.centroid1()
if round(centroid[0])==58 and round(centroid[1])==69:
    print('beam test passed')
else:
    raise Exception('beam test failed')




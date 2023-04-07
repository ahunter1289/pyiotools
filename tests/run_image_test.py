# Image test
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
tl.plot_image(img_file)
tl.plot_image(os.path.join(os.getcwd()[0:-6], 'data','file_example_TIFF_1MB.tiff'))
tl.plot_image(os.path.join(os.getcwd()[0:-6], 'data','2Selected-image-of-laser-beam-profile-for-test-example.png'))

print('image test passed')


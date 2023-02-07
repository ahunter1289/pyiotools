# -*- coding: utf-8 -*-

# Imports
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas
import h5py
import scipy
import math
import tkinter as tk
from tkinter import filedialog
from PIL import Image

plt.close('all')

# Path config
rootdir = '/Users/andrewhunter/offlinedocs/swdev/pyiotools'
testdatadir = '/Users/andrewhunter/offlinedocs/swdev/pyiotoolstestdata'
sys.path.append(rootdir + "/config")
sys.path.append(rootdir + "/tools")

# Tools import
from pyiotools import *

# Analysis
# place code here for data analysis

filename = '/Users/andrewhunter/offlinedocs/swdev/pyiotoolstestdata/beamtestdata/airydisk-rings.jpg'
#filename = '/Users/andrewhunter/offlinedocs/swdev/pyiotoolstestdata/beamtestdata/Selected-image-of-laser-beam-profile-for-test-example.png'
beamimage = plotimage(filename)

testimageclass = FarFieldGaussImage(filename)
#testimageclass._img.show()

#Print the image format
print('Image Format: ' ,testimageclass._img.format)

# Test Centroid Method

centroidtest = testimageclass.centroid1()




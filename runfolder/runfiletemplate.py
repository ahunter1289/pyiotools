# -*- coding: utf-8 -*-

# Basic imports
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas
import h5py
import scipy

# Path config
rootdir = '/Users/andrewhunter/offlinedocs/swdev/pyiotools'
testdatadir = '/Users/andrewhunter/offlinedocs/swdev/pyiotoolstestdata'
sys.path.append(rootdir + "/config")
sys.path.append(rootdir + "/tools")

# Tools import
from importtools import *

# Analysis
# place code here for data analysis
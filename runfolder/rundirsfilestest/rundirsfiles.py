#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 21:23:33 2023

@author: andrewhunter
"""

#imports

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

# Path config
rootdir = '/Users/andrewhunter/offlinedocs/swdev/pyiotools'
testdatadir = '/Users/andrewhunter/offlinedocs/swdev/pyiotoolstestdata'
sys.path.append(rootdir + "/config")
sys.path.append(rootdir + "/tools")

# Tools import
from importtools import *
from dirsfilestools import *

# Analysis
# place code here for data analysis

dirsfiles1 = dirsfiles('/Users/andrewhunter/offlinedocs/swdev/pyiotools/runfolder')
dirsfiles2 = dirsfiles()
dirsfiles3 = dirsfiles('test','test')
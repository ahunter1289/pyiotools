#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 14:04:34 2023

@author: andrewhunter
"""

# Basic imports
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
from pyiotools import *

# Analysis
resultstest1 = importcsv(testdatadir + '/csvtestdata/csvtest/csvtest.csv')
resultstest2 = importcsv()
resultstest3 = importcsv('test','test')
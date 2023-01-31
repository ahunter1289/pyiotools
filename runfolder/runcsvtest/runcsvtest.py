#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 14:04:34 2023

@author: andrewhunter
"""

# Basic imports
import os
import sys

# Set the root directory at the pyiotools level
rootdir = '/Users/andrewhunter/offlinedocs/swdev/pyiotools'
print('rootdir is set: ' + rootdir)

# Load the config/tools

runfile(rootdir + '/config/spydersysmain.py')
print('Config has been loaded')
    
matrix = importcsv(rootdir + '/runfolder/runcsvtest/testdata/csvtest/csvtest.csv')
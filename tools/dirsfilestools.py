#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 20:09:17 2023

@author: andrewhunter
"""

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

def dirsfiles(*dirpath):
    
    if len(dirpath)==0:

        root = tk.Tk()
        root.withdraw()

        dirpath = filedialog.askdirectory()
        
    elif len(dirpath)==1:
        dirpath = dirpath[0]
        
    else:
        raise Exception('Too many arguments provided to dirsfiles')
        
    
    dirsfileslist=os.listdir(dirpath)
    return dirsfileslist
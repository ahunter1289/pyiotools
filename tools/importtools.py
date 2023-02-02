# -*- coding: utf-8 -*-

# plt.close('all')
# %reset
# clear

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

def importcsv(*filepath):
    
    if len(filepath)==0:

        root = tk.Tk()
        root.withdraw()

        filepath = filedialog.askopenfilename()
        
    elif len(filepath)==1:
        filepath = filepath[0]
        
    else:
        raise Exception('Too many arguments provided to importcsv')
        
    
    file=open(filepath)
    reader = csv.reader(file)
    csvdata = []
    for row in reader:
        csvdata.append(row)
    file.close()
    return csvdata

def plotimage(filepath):
    
    image = plt.imread(filepath)
    plt.figure()
    plt.imshow(image)
    
    return image

def importfits(filepath):
    
    return
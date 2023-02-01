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

def importcsv(filepath):
    
    file = open(filepath)
    reader = csv.reader(file)
    listmat = []
    for row in reader:
        listmat.append(row)
    file.close()
    return listmat

def plotimage(filepath):
    
    image = plt.imread(filepath)
    plt.figure()
    plt.imshow(image)
    
    return image

def importfits(filepath):
    
    return
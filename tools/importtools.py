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
from PIL import Image

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

class FarFieldGaussImage(object):
    def __init__(self,imgfile):
        
        img=Image.open(imgfile)
        
        if img.format == 'PNG':
            raise Exception('PNG image types are not compatible with the calculations in this class. In order to resolve this Andy needs to figure out why np.asarray doesnt return RGBA array ([m,n,4]) for png filetypes')
        
        self._img=img
        
    def __str__(self):
        return f"INSERT SELF OUTPUT HERE"
    
    def method1(self):
        return self._img.method1()
    
    def centroid1(self):
        grayarray = self._img.convert('LA')
        grayarray = np.asarray(grayarray)
        grayarray = grayarray[:,:,0]
        rows = len(grayarray[:,0])
        cols = len(grayarray[0,:])
        
        # find row location of centroid
        num=0
        den=0
        for i in list(range(0,rows)):
            # sum of the product of the pixel location and pixel value divided by the sum of all pixel values
            rowsum = sum(grayarray[i,:])
            num=num+i*rowsum
            den=den+rowsum
            
        rowcent = num/den
        
        num=0
        den=0
        for i in list(range(0,cols)):
            # sum of the product of the pixel location and pixel value divided by the sum of all pixel values
            colsum = sum(grayarray[:,i])
            num=num+i*colsum
            den=den+colsum
            
        colcent = num/den
        
        centroid = [rowcent, colcent]
        print('Centroid (weighted average, all pixels) = ', centroid)
        
        return centroid
        
        
        
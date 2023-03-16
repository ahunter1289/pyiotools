# pyiotools
# Author: Andy Hunter

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

def files_w_string(*dirpath,search_strings,**kwargs):

    # In this function we want to pass dirpath which is either a single 
    # directory or a list of directories. Then search the directories for the
    # files that contain the strings in searchstrings in the file name
    # add an option recursive argument

def get_row_data(data_row_header,head_search_val,**kwargs)

    # Pass the function a matrix nxm list where the first column is the
    # row header and the remaining cols are data. Then search the header
    # column for the for the head_search_val and where there is a match, return
    # the data in the remaining columns as a list. THere is optional 
    # argument of return_cols which sets the number of columns you want to
    # return. If you dont pass this argument it returns all data columns
    
def get_col_data(data_col_header,head_search_val,**kwargs)

    # Pass the function a matrix nxm list where the first row is the
    # column header and the remaining rows are data. Then search the header
    # row for the for the head_search_val and where there is a match, return
    # the data in the remaining rows as a list. THere is optional 
    # argument of return_rows which sets the number of rows you want to
    # return. If you dont pass this argument it returns all data rows

def import_csv(*filepath):
    '''
    Import csv file and return as a list
    '''
    
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

def plot_image(*filepath):
    '''
    Import an image on plot
    '''
    
    if len(filepath)==0:

        root = tk.Tk()
        root.withdraw()

        filepath = filedialog.askopenfilename()
        
    elif len(filepath)==1:
        filepath = filepath[0]
        
    else:
        raise Exception('Too many arguments provided to plotimage')
    
    image = plt.imread(filepath)
    plt.figure()
    plt.imshow(image)
    
    return image

def scan_tree(*dirpath,**kwargs):
    ''' 
    Develop a list of dirs, files, and symlinks
    
    If no recursive argument is passed then it will return results from
    subdirectories
    
    recursive=0 will not return results from subdirectories
    recursive=1 will return results from subdirectories
    
    Returns a list of list of string paths [directories, files, symlinks]
    '''
    
    if len(dirpath)==0:

        root = tk.Tk()
        root.withdraw()

        dirpath = filedialog.askdirectory()
        
    elif len(dirpath)==1:
        dirpath = dirpath[0]
        
    else:
        raise Exception('Too many arguments provided to scantree')
     
    if len(kwargs)==0 or ('recursive' in kwargs.keys() and kwargs['recursive']==1):
        rec=1
        print('Running scantree recursively')
    elif 'recursive' in kwargs.keys() and kwargs['recursive']==0:
        rec=0
        print('Running scantree non-recursively')
    else:
        raise Exception('Incorrect arguments passed to scantree')  
     
    fileslist=[]
    dirslist=[]
    dirslist.append(dirpath)
    symlinklist=[]
    def scan_recurse(dirpath,rec):
        
        for entry in os.scandir(dirpath):
            if entry.is_file():
                yield os.path.join(dirpath, entry.name)
            elif entry.is_symlink():
                symlinklist.append(os.path.join(dirpath,entry.name))
            else:
                dirslist.append(os.path.join(dirpath,entry.name))

                if rec:
                    yield from scan_recurse(entry.path,rec)          
                          
    for i in scan_recurse(dirpath,rec):
        fileslist.append(i)
    return [dirslist,fileslist,symlinklist]

class FarFieldGaussImage(object):
    '''
    Far Field Gaussian beam image
    
    Object provides methods such as calculating centroid. Methods include:
        centroid1: a weighted average centroid of entire image
    '''
    
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
        
        
        
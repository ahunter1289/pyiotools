# plt.close('all')# %reset# clear# Basic importsimport osimport sysimport matplotlib.pyplot as pltimport numpy as npimport csvimport pandas as pdimport h5pyimport scipyimport math# Path configrootdir = '/Users/andrewhunter/offlinedocs/swdev/pyiotools'testdatadir = '/Users/andrewhunter/offlinedocs/swdev/pyiotoolstestdata'sys.path.append(rootdir + "/config")sys.path.append(rootdir + "/tools")# Tools importfrom pyiotools import *# Analysisimage = plotimage('/Users/andrewhunter/offlinedocs/swdev/pyiotoolstestdata/tifftestdata/file_example_TIFF_1MB.tiff')
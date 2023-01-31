#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 16:49:10 2022

@author: andrewhunter
"""

import h5py

import numpy as np
f = h5py.File("mytestfile.hdf5", "w")
list(f.keys())
# -*- coding: utf-8 -*-

import csv

def importcsv(filepath):
    
    file = open(filepath)
    reader = csv.reader(file)
    listmat = []
    for row in reader:
        listmat.append(row)
    file.close()
    return listmat

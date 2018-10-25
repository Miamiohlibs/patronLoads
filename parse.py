import os, csv
import numpy as np
from jsonschema import validate

def parse():
    import csv
    datafile = open('a.csv', 'r')
    datareader = csv.reader(datafile, delimiter='\n')
    datafile.close()
    data = []

    #this will write file to array
    for row in datareader:
        data.append(row)
    
    b = np.reshape(data, (-1,11)) #reshapes as nested array on 11 columns each
    #may need to add another nested array varFields, leaving expDate, ptype, and patron codes at highest 

    #remove trailing white space
    b = np.char.rstrip(b, ' ')
    
    #shouldn't need to store post-split array; 
    #use array slices during writing to schema
    #for i in b:
    #    slice = i[0][15:]
    #    np.insert(i,0,slice)
    
    #outputs new np array but inserting the expirationDate as an additional array slice

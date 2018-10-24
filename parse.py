import os, csv
import numpy as np

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
    
    #need to parse the first row in each array
    for i in b :
        i = str.split(i[0], 'none   ')#doesn't work; find alternate

   #shouldn't need to store split array; 
   #use array slices during writing to schema

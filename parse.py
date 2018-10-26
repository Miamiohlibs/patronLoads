import os, csv
import numpy as np
from jsonschema import validate #use to validate each array slice writing to api

def parse():
    datafile = open('patrons.csv', 'r')
    datareader = csv.reader(datafile, delimiter='\n')
    data = []

    #this will write file to array
    for row in datareader:
        data.append(row)
    datafile.close()

    b = np.reshape(data, (-1,11)) #reshapes as nested array on 11 columns each
    #remove trailing white space; no need to reshape or trim since we can do this during schema write
    b = np.char.rstrip(b, ' ')
    
    #store raw ptfs data in array; shouldn't need to store post-split array
    #use array slices during writing to schema
    #for i in b:
    #    slice = i[0][15:]
    #    np.insert(i,0,slice)
    
    #outputs new np array but inserting the expirationDate as an additional array slice
    for i in b:
        expirationDate = i[0][16:]
        patronType = i[0][]
        patronCodes = i[0][]
        pcode1 = i[0][]
        pcode2 = i[0][]
        pcode3 = i[0][]
        barcode = 
        tap = 
        soc = 
        uniqueId = 
        email = 
        address = 
        home = 
        name = 
        campusPhone = 
        phone = 
        {'expirationDate': '2019-07-01', 'patronType': 2, 'patronCodes': {'pcode1': '8', 'pcode2': '0', 'pcode3': 0}, 'varFields': [{'fieldTag': 'b', 'content': '+01620000'}, {'fieldTag': 'b', 'content': '987000123456789'}, {'fieldTag': 's', 'content': '+01600000'}, {'fieldTag': 'u', 'content': 'uniqueId'}, {'fieldTag': 'z', 'content': 'student@miamioh.edu'}, {'fieldTag': 'a', 'content': 'LIBRARY, KING$CAMPUS MAIL OH 00000'}, {'fieldTag': 'h', 'content': '1059 Street AVE$Dayton OH 45377-1471'}, {'fieldTag': 'n', 'content': 'Zmuda Bob'}, {'fieldTag': 't', 'content': '513529000'}, {'fieldTag': 'p', 'content': '937232000'}]}





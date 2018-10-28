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
    patron = {}

    for i in b:
        ##determine what location in the patron leader field for the following
        ##patron fields
        patron["patronType"] = i[0][]
        patron["patronCodes"]["pcode1"] = i[0][]
        patron["patronCodes"]["pcode2"] = i[0][]
        patron["patronCodes"]["pcode3"] = i[0][]

        patron["expirationDate"] = i[0][16:]
        plus = {"fieldTag":"b","content":i[9][1:]}
        barcode = {"fieldTag":"b","content":i[10][1:]}
        soc = {"fieldTag":"s","content":i[6][1:]}
        uniqueId = {"fieldTag":"u","content":i[8][1:]}
        email = {"fieldTag":"z","content":i[7][1:]}
        address = {"fieldTag":"a","content":i[2][1:]}
        home = {"fieldTag":"h","content":i[4][1:]}
        name = {"fieldTag":"n","content":i[1][1:]}
        campusPhone = {"fieldTag":"t","content":i[3][1:]}
        phone = {"fieldTag":"p","content":i[5][1:]}
        patron["varFields"] = [plus,barcode,soc,uniqueId,email,address,home,name,campusPhone,phone]
        #print(patron)

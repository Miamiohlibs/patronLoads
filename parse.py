import os, csv
import numpy as np
from jsonschema import validate #use to validate each array slice writing to api
import get_token

##the purpose of this file is to parse a basic tsv patron file given to a
##library from central IT containing all of the patrons into json api calls
##to the Sierra patron api

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
    #add more to schema for length of integers/char
    schema = {
          "expirationDate": "string",
          "patronType": "integer",
          "patronCodes": {
            "pcode1": "integer",
            "pcode2": "integer",
            "pcode3": "integer",
          },
          "varFields": [
            {
              "fieldTag": "char",
              "content": "string"
            }

          ]
        }

    for i in b:
        ##determine what location in the patron leader field for the following
        ##patron fields

        #building patron json file for each 11 row patron record from patron.csv
        patron["expirationDate"] = i[0][16:]
        patron["patronType"] = i[0][3] #0002
        patron["patronCodes"] = {} #will be filled below
        patron["patronCodes"]["pcode1"] = i[0][4] #00028
        patron["patronCodes"]["pcode2"] = i[0][5] #000031
        patron["patronCodes"]["pcode3"] = i[0][6]
        #fieldTags
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
        print(patron)
        #validate json schema; look for raised exception
        #if
        validate(patron,schema)


            #lookup to see if this is a new patron; %2b is the + symbol converted, add the soc
            url = "https://holmes.lib.miamioh.edu:443/iii/sierra-api/v4/patrons/find?varFieldTag=s&varFieldContent={}".format(i[6][1:])
            #need to url encode url

            #if patron is found retrieve Sierra patron ID number
            #preprend Sierra patron ID to the beginning of the patron json file
            #then write to Sierra update patron API
            url = "https://holmes.lib.miamioh.edu:443/iii/sierra-api/v4/patrons/{}".format(SierraPatronID)

            #if patron is not located write to create application
            url = "https://holmes.lib.miamioh.edu:443/iii/sierra-api/v4/patrons/"

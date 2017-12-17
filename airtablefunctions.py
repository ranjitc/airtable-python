#!/usr/bin/python3
# coding=utf-8
#below line is required for apache webservers only
#print "Content-Type: text/html\n"

import requests
import urllib
import constants
import json

###get all records function
def getRecords(tbl, params):

    if (params == "none") or (params == ""):
        params = ''
    else:
        params = urllib.parse.urlencode(params)

    if (tbl == "none") or (tbl == ""):
        return "Error: table cannot be \"\""

    # if table name has a space, replace with %20
    tbl = tbl.replace(" ","%20")

    offset = "&offset="

    recordArray = []


    while True:

        # airtable api returns an offset key if there are more than 100 records
        # if found we collect all responses till offset is not returned

        uri = constants.uri+tbl+'?'+params+offset

        r = requests.get(uri, headers=constants.fetchheaders)

        response = r.json()

        try:
            recordArray = recordArray + response['records']
        except KeyError:
            print ("Error: \r\n"+str(response))


        # to get next set of results the offset value must be used in api call

        if 'offset' in response:
            offset = "&offset="+response['offset']
        else:
            break

    return recordArray
###

###get field from records
def getField(response, fieldName, delimiter):

    if (response == "") or (fieldName == ""):
        return "Error response / fieldName cannot be \"\""

    newresponse = []

    ### default record separator
    if (delimiter == "none") or (delimiter == ""):
        delimiter = "\r\n"

    #its imp to define recordno & item both, even if item is not used
    for recordno, item in enumerate(response):
    	newresponse.append(response[recordno]['fields'][fieldName])

    if (delimiter == "array") or (delimiter == "list"):
        return newresponse
    else:
        return delimiter.join(newresponse)

###

###get id from records
def getId(response, delimiter):

    if (response == ""):
        return "Error response cannot be \"\""

    newresponse = []

    ### default record separator
    if (delimiter == "none") or (delimiter == ""):
        delimiter = "\r\n"

    #its imp to define recordno & item both, even if item is not used
    for recordno, item in enumerate(response):
    	newresponse.append(response[recordno]['id'])

    if (delimiter == "array") or (delimiter == "list"):
        return newresponse
    else:
        return delimiter.join(newresponse)

###

###get createdTime from records
def getCreatedTime(response, delimiter):

    if (response == ""):
        return "Error: response cannot be \"\""

    newresponse = []

    ### default record separator
    if (delimiter == "none") or (delimiter == ""):
        delimiter = "\r\n"

    #its imp to define recordno & item both, even if item is not used
    for recordno, item in enumerate(response):
    	newresponse.append(response[recordno]['createdTime'])

    if (delimiter == "array") or (delimiter == "list"):
        return newresponse
    else:
        return delimiter.join(newresponse)

###

### get record

def getRecord(tbl, recordId):

    # easy way to check if any parameter is not defined
    for i in locals().values():
        if i == "":
            return "Error: values must not be \"\""

    # if table name has space replace with %20
    tbl = tbl.replace(" ","%20")

    uri = constants.uri+tbl+"/"+recordId

    r = requests.get(uri, headers=constants.fetchheaders)

    response = r.json()

    return response

###

### create records

def createRecord(tbl, data):

    # easy way to check if any parameter is not defined
    for i in locals().values():
        if i == "":
            return "Error: values must not be \"\""

    # if table name has space replace with %20
    tbl = tbl.replace(" ","%20")

    uri = constants.uri+tbl

    r = requests.post(uri, headers=constants.postheaders, data=json.dumps(data))

    response = r.json()

    return response

###

### patch records

def patchRecord(tbl, recordId, data):

    # easy way to check if any parameter is not defined
    for i in locals().values():
        if i == "":
            return "Error: values must not be \"\""

    # if table name has space replace with %20
    tbl = tbl.replace(" ","%20")

    uri = constants.uri+tbl+"/"+recordId

    r = requests.patch(uri, headers=constants.postheaders, data=json.dumps(data))

    response = r.json()

    return response

###

### put records

def putRecord(tbl, recordId, data):

    # easy way to check if any parameter is not defined
    for i in locals().values():
        if i == "":
            return "Error: values must not be \"\""

    # if table name has space replace with %20
    tbl = tbl.replace(" ","%20")

    uri = constants.uri+tbl+"/"+recordId

    r = requests.put(uri, headers=constants.postheaders, data=json.dumps(data))

    response = r.json()

    return response

###

### delete records

def deleteRecord(tbl, recordId):

    # easy way to check if any parameter is not defined
    for i in locals().values():
        if i == "":
            return "Error: values must not be \"\""

    # if table name has space replace with %20
    tbl = tbl.replace(" ","%20")

    uri = constants.uri+tbl+"/"+recordId

    r = requests.delete(uri, headers=constants.postheaders)

    response = r.json()

    # if deletion is sucessful airtable returns deleted == True
    if 'deleted' in response:
        if (response['deleted'] == True):
            return response
        else:
            return "Error in deletion"
    else:
        return "Error in query"

###

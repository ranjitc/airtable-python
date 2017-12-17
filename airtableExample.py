#!/usr/bin/python3
# coding=utf-8
#below line is required for apache webservers only
#print "Content-Type: text/html\n"

# import functions from airtablefunctions.py and assign it as atf
import airtablefunctions as atf
# since json already present in airtable functions, but call json for easier writing
from airtablefunctions import json

#call functions

# define table name or write directly in function
exampleTable = "myTable"

#build parameters

# filter list is what your query to airtable will be
# refer to https://codepen.io/airtable/full/rLKkYB to get
# an idea of parameters that can be used

filterlist =    {
                "fields[0]" : "nameOfField1",
                "fields[1]" : "nameOfField2",
                "sort[0][field]"  : "sortField",
                "sort[0][direction]" : "asc",
                "maxRecords" : "3",
                }

result = atf.getRecords(exampleTable, filterlist)
print (json.dumps(result))

fields = atf.getField(result,'nameOfField1','list')
print (json.dumps(fields))

ids = atf.getId(result, 'array')
print (ids)

createdTimes = atf.getCreatedTime(result, 'list')
print (createdTimes)


# create data to post
# note: airtable by default does not change type
# of data being posted
# if you want to ensure that data being entered is changed
# to the correct type by airtable instead of your code
# make sure to set typecast to true

recorddata = { "fields": {"nameOfField1": "valueForField1",
                         "nameOfField2": "valueForField2"},
              "typecast": True
             }

createdRecord = atf.createRecord(exampleTable,recorddata)

print (json.dumps(createdRecord))
print ("\r\n")
print (json.dumps(createdRecord['fields']))
print (createdRecord['id'])
print (createdRecord['createdTime'])

# to fetch a single record, we need its id
# we can use the id returned in the above example

createdId = createdRecord['id']

# once you have an id you can fetch that record

getarecord = atf.getRecord(exampleTable,createdId)

print (json.dumps(getarecord))

# patch data implies that you can update only
# selected fields without affecting / changing
# fields which are not mentioned

patchdata = { "fields": {"nameOfField1": "valueForField1",
                         "nameOfField2": "valueForField2"},
             "typecast": True
            }


patchedRecord = atf.patchRecord(exampleTable,createdId,patchdata)

print (json.dumps(patchedRecord))


# put data implies that fields not mentioned will be
# set to "" / cleared

putdata = { "fields": {"nameOfField1": "valueForField1",
                         "nameOfField2": "valueForField2},
            "typecast": True
           }

updatedRecord = atf.putRecord(exampleTable,createdId,putdata)

print (json.dumps(updatedRecord))


# if delete is not sucessfule error will be returned

deletedRecord = atf.deleteRecord(exampleTable,createdId)

print (json.dumps(deletedRecord))



# example of creating a filterlist which returns only
# those records which match a criteria
# the criteria needs to be defined using airtable formulae
# which are explained here -https://support.airtable.com/hc/en-us/articles/203255215-Formula-field-reference

filterlist =    {
                "fields[0]" : "nameOfField1",
                "fields[1]" : "nameOfField2",
                "sort[0][field]"  : "sortField",
                "sort[0][direction]" : "asc",
                "filterByFormula": "OR(nameOfField3 != 'Completed', nameOfField4 != 'name')",
                }


# this will return all values of field1 & field2 where either field3 is not equal to Completed or
# field for is not equal to name

result = atf.getRecords(exampleTable, filterlist)
print (json.dumps(result))

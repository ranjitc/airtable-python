**Python functions to filter, get, create, patch, put(update) and delete Airtable Data**

*Brief Explanation*

1. Prepare constants file
	1. Enter api, app values for your database
	2. You can get these values from airtable.com/api on logging in
	3. App value will change with your base, Api value with your account
	4. Keep other constant values as is

2. Create a new python file and import json and airtablefunctions. Files should be in same directory. You can import files in many ways. Look at https://stackoverflow.com/questions/6695798/what-is-the-difference-between-from-random-import-and-import-random-random for clarification.

Since airtablefunctions in our case has ONLY functions and constants (which anyways should not be changed or reused for our use case) it is safe to use:
``` 
from airtablefunctions import *
```
but for the sake of clarity it is better to use:
``` 
import airtablefunctions as atf
```
this allows us to use atf. in code instead of airtablefunctions. this does have some limitations but it does not affect us as we are not going to update or call any values from airtablefunctions out of the predefined use.

if json is not explicity imported then it will have to be called as atf.json or airtablefunctions.json depending on how you have imported airtablefunctions

to simplify this import json from airtablefunctions using its own name of json, with this method you can simply call json as json
```
from airtablefunctions import json
```
you could also import json directly
```
import json
```

to summarise
```
import airtablefunctions as atf
from airtablefunctions import json
```

3. Call functions as required. Following are explanations

    1. getRecords - this returns a list of records from the specified table and filtered by parameters. Parameters are to be in a dict format and needs to follow Airtable Filter By Formula Guidelines. Look at airtableExample.py for examples or refer to https://codepen.io/airtable/full/rLKkYB . Table name is compulsary but parameters are not. Even though Airtable limits record calls to 100, this function returns all records

    2. getField - this returns values of a field, from the records which have been returned above. It takes the list as a parameter, the field Name and a delimiter. If no delimiter is specified it returns values separated by new lines. If delimiter is specified as list or array it returns a list of field values. If you delimit int fields then they may be converted to string or throw an error.

	3. getId - similar to above but returns record Ids

	4. getCreatedTime - similar but for createdTime

	5. getRecord - This returns a single record from a table, given the record Id. Useful if you want to lookup a value which is defined as a lookup field in airtable. This is because airtable returns record ids instead of values for lookup fields. Better way is to design your airtable with formula fields which lookup the value and get those directly. Look at solutions proposed by Leslie_Henry and Alexander_Sorokin on [this airtable post](https://community.airtable.com/t/record-id-showing-instead-of-value/412)

	6. createRecord - This creates a record as per data given. data is in the same format as for flter, which is a dict.

	7. patchRecord - This updates only the specified fields for a given record. It leaves unspecified fields untouched.

	8. putRecord - This updates the entire record. Unspecified fields (other than formula and auto-generated fields) are deleted

	9. deleteRecord - This deletes a record. It returns a deleted true key if sucessful.


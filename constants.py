api = 'yourapikey'
app = 'your database id, check the airtable url for appxxx'
url = 'https://api.airtable.com/v0/'
fetchheaders = {'Authorization': 'Bearer '+api}
uri = url+app+'/'
postheaders = {'Authorization': 'Bearer '+api,'Content-type': 'application/json'}

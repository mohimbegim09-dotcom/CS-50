import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get('https://itunes.apple.com/search?entity=song&limit=1&term=' + sys.argv[1])
print(json.dumps(response.json(), indent=2))    
#indent=2 is used to format the JSON output 
# with an indentation of 2 spaces for better readability.

#json.dumps() is a method that converts a Python object 
# into a JSON string.

#OR 
# if you want to specify on smth, e.g tracks 
# instead of just using print, you can

o = response.json()
for result in o['results']:
    print(result['trackName'])
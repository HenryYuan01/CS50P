import json 
import requests
import sys

if len(sys.argv) != 2: 
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])
# this prints everything 
# print(json.dumps(response.json(), indent=2))

# this prints only the track lists 
o = response.json() 
for result in o["results"]: 
    print(result["trackName"])
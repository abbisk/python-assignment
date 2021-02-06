'''Write a Python program to convert the Python dictionary object (sort by key) to
JSON data. Print the object members with indent level 4.'''

import json
dictnr = {'Apple': 5, 'Banana': 7, 'Papaya': 3, 'Grapes': 4}

print("Dictionary :", dictnr)
print("json: ")
print(json.dumps(dictnr, sort_keys=True, indent=4))


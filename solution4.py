''' 
Write a Python program to sort a list of dictionaries using Lambda.

Original list of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2',
'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
Sorting the List of dictionaries :
[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7,
'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
'''

def sort_listof_dicts(listofdicts):

    print("Original list of dictionaries : ")
    print(listofdicts)
    print()
    sortedlistofdict = sorted(listofdicts, key = lambda c: c['color'])

    print("Sorting the List of dictionaries : ")
    return sortedlistofdict



# Driver code 
listofdicts = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2',
'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

print(sort_listof_dicts(listofdicts))

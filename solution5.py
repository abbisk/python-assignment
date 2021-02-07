'''
Write a Python program that takes a text file as input and returns the number of
words of a given text file.
Note: Some words can be separated by a comma with no space.
'''

def word_count(fpath):
    with open(fpath) as file:
        data = file.read()
        data.replace(",", " ")
        data.replace(", ", " ")
        return len(data.split(" "))

# Driver code
print(word_count("file.txt"))
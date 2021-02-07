'''
Write a Python program that takes a text file as input and returns the number of
words of a given text file.
Note: Some words can be separated by a comma with no space.
'''

count = 0
file = open("file.txt", "r")  

#Gets each line till end of file is reached  
for line in file: 
    words = line.split(" ")
    count = count + len(words)

print("Number of words present in given file: " + str(count))
file.close()
# Write a Python program to read a file line by line and store it into a list.

def file_read(fname):
    lines = []
    with open(fname) as file:
        for line in file:
            lines.append(line)
    return lines

file = file_read('file.txt')
print(file)
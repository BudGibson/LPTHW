# import the argv module from sys
from sys import argv

# load some variables from argv
script, filename = argv

# put the filehandle designated by filename in a variable txt
txt = open(filename)

# print the name of the file
print(f"Here's your file {filename}:")
# print the contents of the file as read in using the read method
print(txt.read())
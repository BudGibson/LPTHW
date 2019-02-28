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

# Prompt for the filename via the terminal
print("Type the filename again:")
# Read the filename into the variable file_again
file_again = input("> ")

# put the filehandle designated by file_again in a variable txt_again
txt_again = open(file_again)

# print the contents of the file as read in using the read method
print(txt_again.read())
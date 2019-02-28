# Prompt for the filename via the terminal
print("Type the filename to print:")
# Read the filename into the variable file_again
file_again = input("> ")

# put the filehandle designated by file_again in a variable txt_again
txt_again = open(file_again)

# print the contents of the file as read in using the read method
print(txt_again.read())
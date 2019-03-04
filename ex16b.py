from sys import argv

script, filename = argv

contents = open(filename)

print(f"Now, let's see the contents of {filename}:")
print(contents.read())
contents.close()
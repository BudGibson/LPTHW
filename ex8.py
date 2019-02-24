# Create a string to interpolate variables
formatter = "{} {} {} {}"

# Interpolate integers into formatter and print
print(formatter.format(1, 2, 3, 4))

# Interpolate strings into formatter and print
print(formatter.format("one", "two", "three", "four"))
# Interpolate logical values into formatter and print
print(formatter.format(True, False, False, True))
# Interpolate the string formatter into formatter and print
print(formatter.format(formatter, formatter, formatter, formatter))
# Interpolate 4 strings into formatter using separate lines and print
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

test = formatter.format(1, 2, 3, 4)
print(test)
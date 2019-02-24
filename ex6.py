# set a variable equal to 10
types_of_people = 10
# create a formatted string interpolating types_of_people and place it in a variable
x = f"There are {types_of_people} types of people."

# set a variable equal to the string binary
binary = "binary"
# set a variable equal to the string don't
do_not = "don't"
# create a formatted string interpolating the variables binary and do_not
y = f"Those who know {binary} and those who {do_not}."

# print x
print(x)
#print y
print(y)

# print a string interpolating x
print(f"I said: {x}")
# print a string interpolating y
print(f"I also said: '{y}'")

# set hilarious to the logical value false
hilarious = False
# Create a string with a place to insert an interpolated variable
joke_evaluation = "Isn't that joke so funny?! {}"

# print the string interpolating the variable hilarious
print(joke_evaluation.format(hilarious))

# create a string w
w = "This is the left side of.."
# create a string e
e = "a string with a right side."

# print the concatenation of w and e
print(w + e)
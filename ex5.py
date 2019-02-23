name = 'Bud Gibson'
age = 58 # not a lie
height = 68 # inches
height_cm = height * 2.54 # centimeter height
weight = 174 #lbs
weight_kg = 174/2.2 # kg weight
eyes = 'Brown'
teeth = 'White'
hair = 'Gray'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"That's roughly {int(height_cm)} cm.")
print(f"He's {weight} pounds heavy.")
print(f"That's roughly {int(weight_kg)} kg.")
print(f"Actually, that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usally {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
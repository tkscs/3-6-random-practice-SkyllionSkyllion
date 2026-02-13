# Make a random pet.
import random
# Choose:
# Type of animal (at least 3 choices, string)
animal = random.choice(["fish", "panda", "ido", "aron", "cat", "zeke"])#REPLACE THIS WITH YOUR CODE
# Age (integer)
age = random.randint(0,1000) #REPLACE THIS WITH YOUR CODE
# Color (at least 3 choices, string)
# Weight (float)
weight = random.uniform(0,1000)#REPLACE THIS WITH YOUR CODE

# Print a summary of your pet using an f-string
print(f"Your pet is a {animal} that is {age} years old and weighs {weight} pounds")#REPLACE THIS WITH YOUR CODE

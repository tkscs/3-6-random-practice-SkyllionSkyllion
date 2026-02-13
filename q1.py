import random
colors = ["red", "green", "yellow", "blue"]
sides = ["left", "right"]
appendage = ["hand", "foot"]

def spin_twister_spinner():
  """
  Returns a list with a random color, side, and appendage
  
  colors: "red", "green", "yellow", or "blue"
  sides: "left" or "right"
  appendage: "hand" or "foot"
  """
  #YOUR CODE HERE
  first = random.choice(colors)
  second = random.choice(sides)
  third = random.choice(appendage)
  return(f"{first}, {second}, {third}")
  


# Here's the function call. This should print a random assortment of twister commands
for _ in range(10):
  print(spin_twister_spinner())
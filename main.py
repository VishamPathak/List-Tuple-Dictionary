import random

pizzaToppings = ["pineapple", "pepperoni", "olives", "mushrooms", "bellpeppers", "bacon"]

print(len(pizzaToppings))

print(pizzaToppings[2])

pizzaToppings.append("extra cheese")
pizzaToppings.remove("mushrooms")
pizzaToppings.insert(5, "spinach")
pizzaToppings.pop(2)

print(len(pizzaToppings))
print(pizzaToppings)

index = 0
while(index < len(pizzaToppings)):
  print(pizzaToppings[index])
  index += 1

for index in pizzaToppings:
  print(index)

for letters in pizzaToppings[4]:
  print(letters)

print(pizzaToppings[random.randint(0, len(pizzaToppings)-1)])

teacher = {}
teacher["name"] = "Celine"
teacher["favorite color"] = "Yellow"
teacher["favorite fruit"] = "Banana"
teacher["height"] = "5'2"

print(teacher)
print(teacher["favorite fruit"])
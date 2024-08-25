# If elif Else condition examples

#================================================== Ex 1 of Roller Coaster====================================

# print("Welcome to the Roller Coaster!")
# height = int(input("What is your height in cm? "))
# bill = 0
# if height >= 120:
#   print("You can ride the roller coaster")
#   age = int(input("What is your age? "))
#   if age < 12:
#     bill += 5
#     print(f"Child tickets are {5}")
#   elif age <= 18:
#     bill += 7
#     print(f"Youth tickets are {7}")
#   elif age >= 45 and age <= 55:
#     bill += 0
#     print("Everything is going to be ok. Your ticket is free, Have a free ride on us!")
#   else:
#     bill += 12
#     print(f"Adult ticket price is ${12}")
#   wanna_photo = input("Do you want a photo taken? Y or N. ")
#   if wanna_photo == "Y":
#     bill += 3
#     print(f"Your total bill is, {bill}")
# else:
#   print("Sorry, you have to grow taller before you can ride.")


#================================================== Ex 2 of Python Pizza Deliveries====================================


# print("Welcome to the Python Pizza Deliveries!")
# size = input("What size of size would you like to order")
# pepporoni_addition = input("Do you want pepperoni? Y or N")
# wannna_extra_cheese = input("Do you want extra cheese? Y or N")

# bill = 0
# if size == "S":
#   bill += 15
# elif size == "M":
#   bill += 20
# else:
#   bill += 25


# if pepporoni_addition == "Y":
#   if size == "S":
#      bill += 2 
#   else:
#     bill += 3

# if wannna_extra_cheese == "Y":
#   bill += 1
# print(f"Your total bill is ${bill}")



#===================================== Ex 3 of Love Calculator =====================================

# print("Welcome to the Name compatibility calculator!")
# name1 = input("Whta is your name? \n")
# name2 = input("What is your cimpanion name? \n")
# #convert uppercase to lowercase
# merge_name = (name1 + name2).lower()

# T = merge_name.count("t")
# r = merge_name.count("r")
# u = merge_name.count("u")
# e = merge_name.count("e")
# true = T + r + u + e

# L = merge_name.count("l")
# o = merge_name.count("o")
# v = merge_name.count("v")
# e = merge_name.count("e")
# love = L + o + v + e

# love_score = int(str(true) + str(love))
# if love_score < 10 or love_score > 90:
#   print(f"Your love score is {love_score}, you go together like coke and mentos.")
# elif love_score >= 40 and love_score <= 50:
#   print(f"Your love score is {love_score}, you are alright together.")
# else:
#   print(f"Your love score is {love_score}")



#===================================Ex 4 of Treasure Island====================================

# print("Welcome to the Treasure Island")
# print("Your mission is to find the treasure")
# step_one = input("You are at a cross road. Where do you want to go? Type 'left' or 'right'\n")
# if step_one.lower() == "left":
#   step_two = input ("You came to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
#   if step_two.lower() == "wait":
#     step_three = input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n")
#     if step_three.lower() == "yellow":
#       print("You found the treasure! You win!")
#     elif step_three.lower() == "blue":
#       print("You enter a room of beasts. Game Over.")
#     elif step_three.lower() == "red":
#       print("It's a room full of fire. Game Over.")
#     else:
#       print("You chose a door that doesn't exist. Game Over.")
#   else:
#     print("You got attacked by an angry trout. Game Over.")
# else:
#   print("You fell into a hole. Game Over.")



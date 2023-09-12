# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# My input
# import random

# len_names = int(len(names))
# random_name = random.randint(0, len_names)

# print(f"{names[random_name]} is going to buy the meal today!")

import random

len_names = len(names)
random_name = random.randint(0, len_names - 1)

print(f"{names[random_name]} is going to buy the meal today!")

#Teacher's input
# #Get the total number of items in list.
# num_items = len(names)
# #Generate random numbers between 0 and the last index. 
# random_choice = random.randint(0, num_items - 1)
# #Pick out random person from list of names using the random number.
# person_who_will_pay = names[random_choice]

# print(person_who_will_pay + " is going to buy the meal today!")

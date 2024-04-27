# PandaBear Coffee Shop Simulator 1000
# Copyright (C) 2024 by PandaBear, Inc. All Rights Reserved.

print("PandaBear Coffee Shop Simulator 1000, Version 1.00")
print("Copyright (C) 2024 PandaBear, Inc. All Rights Reserved\n")
print("Let's collet some information before we start the game.\n")

#Get name and shop name
name = input("What is your name? ")
shop_name =  input("What do you want to name your coffee shop? ")

print("\nThanks " + name + "! Let's set some initial pricing.\n")

#Get initial price of a cup of coffee
cup_price = float(input("How much do you want to charge for a cup of coffee? "))

#Display what we have so far
print("\nGreat! Here is what we have so far:\n")
print("Your name: " + name + " and you're opening a coffee shop called " + shop_name + "!")
print("You're going to charge $" + cup_price + " for your first cup of coffee.\n")

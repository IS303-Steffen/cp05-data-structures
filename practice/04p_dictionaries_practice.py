import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# =====================
# DICTIONARIES PRACTICE
# =====================


# 1. PRACTICE PROBLEM: FRUIT MARKET INVENTORY
# Objective: Create a dictionary to manage the inventory of a fruit market and perform various operations on it.

# Tasks:
#     - Create a dictionary named fruit_inventory where the keys are the names of fruits and the values are the quantities available. Add at least five fruits with their quantities.
#     - Print the entire dictionary.
#     - Find the quantity available for "Apples" and print it. Use the method that handles the case where the key might not exist, providing a default message like "Fruit not found."
#     - Add a new fruit to the inventory with its quantity.
#     - Update the quantity of an existing fruit.
#     - Remove a fruit from the inventory using .pop() and print the name of the fruit along with the quantity removed.
#     - Use .get() to check the quantity of a fruit. If the fruit is not in the inventory, it should return "Fruit not in inventory."
#     - Print only the names of the fruits available in the market using .keys().
#     - Print only the quantities of each fruit using .values().
#     - Check if "Oranges" are available in the market. If yes, print a message saying "Oranges are available!"

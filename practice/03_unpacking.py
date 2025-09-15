from helper_functions import clear_screen
clear_screen()

# =====================
# NESTING LISTS
# =====================


'''
UNPACKING
---------
Sometimes, you want to grab the elements in a list, and put them into
individual variables. This is called "unpacking"

you do it like this:
var1, var2, var3 = example_list

if the number of elemnts in the list doesn't match the number of variables
you are trying to put things into,
it won't work. You can use example_list[0:3], etc if you
only want to grab a part of the list.
'''

# Characters from Harry Potter
harry_potter_characters = [
    "Harry Potter", "Hermione Granger", "Ron Weasley",
    "Albus Dumbledore", "Severus Snape", "Voldemort",
    "Sirius Black", "Dobby", "Luna Lovegood", "Draco Malfoy"
]

# 1. UNPACKING PART OF A LIST
# Put the first 3 characters of the Harry Potter list
# into 3 separate variables, then print each out.





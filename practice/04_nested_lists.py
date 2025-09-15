from helper_functions import clear_screen
clear_screen()

# ============
# NESTED LISTS
# ============

'''
NESTED LISTS
------------
Remember how lists store other variables inside them, each variable is an
element.

Lists themselves are variables. That means they can be elements of lists.
So you can have a list with multiple lists inside it. This is a nested list.
'''

# Characters from Harry Potter
harry_potter_characters = [
    "Harry Potter", "Hermione Granger", "Ron Weasley",
    "Albus Dumbledore", "Severus Snape", "Voldemort",
    "Sirius Black", "Dobby", "Luna Lovegood", "Draco Malfoy"
]

# Characters from Lord of the Rings
lord_of_the_rings_characters = [
    "Frodo Baggins", "Samwise Gamgee", "Aragorn",
    "Legolas", "Gandalf", "Gimli", "Boromir",
    "Sauron", "Galadriel", "Saruman"
]

# Characters from Super Mario
super_mario_characters = [
    "Mario", "Luigi", "Princess Peach", "Bowser",
    "Yoshi", "Toad", "Donkey Kong", "Wario",
    "Waluigi", "Princess Daisy"
]

# 1. CREATE A NESTED LIST
# create a list called nested_list,
# and put each of the 3 above lists inside it. Print it out after.


# 2. ACCESS AN INNER LIST
# Print out the 3rd Lord of the Rings character.
'''
Just like you access elements in a list using brackets [], because the elements
in a nested list are also lists, just use brackets again to access the inner
lists.

nested_list[0] would get you the first list inside nested_list
nested_list[0][0] would get you the first element inside the first list.
'''

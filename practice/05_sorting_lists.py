from helper_functions import clear_screen
clear_screen()

# =============
# SORTING LISTS
# =============

'''
OVERVIEW
--------
Lists allow you to sort them using a few different functions.

When you sort,  it is also helpful to understand that there are largely
two ways functions do what you want:
    - in-place change:
        - This alters the list itself.
    - returning a changed list:
        - This keeps the original list intact, and "returns" you a new list.

In-place sorting:
    - .sort()

Return sorting:
    - sorted()

You can use either, but some might be better for certain situations.
'''

# Characters from Harry Potter
harry_potter_characters = [
    "Harry Potter", "Hermione Granger", "Ron Weasley",
    "Albus Dumbledore", "Severus Snape", "Voldemort",
    "Sirius Black", "Dobby", "Luna Lovegood", "Draco Malfoy"
]


# Print out characters to see how they are originally ordered.
print(harry_potter_characters)


# 1. SORT THE LIST ALPHABETICALLY IN-PLACE:
# Print out the harry potter list in alphabetical order.
'''
You can sort any list using .sort(). Default is either
alphabetical (when list has strings) or ascending (when using numerical data)
If you mix strings and numerical data, .sort() will throw an error.

example_list.sort()
'''


# 2. SORT THE LIST REVERSE ALPHABETICALLY IN-PLACE
# Print out the harry potter list in alphabetical order.
'''
.sort() has a "reverse" parameter. The default value is False. You can change
it to True:

example_list.sort(reverse=True)
'''


# 3. RETURN AND PRINT A NEW ALPHABETICALLY ORDERED LIST:
# Print out a new harry potter list in alphabetical order.
# print out the original harry potter list afterwards.
'''
You can use sorted() to return a new list that is sorted how you want.
This is useful if you want a sorted list, but don't want to affect the original
list:

new_list = sorted(example_list)
'''








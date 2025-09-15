from helper_functions import clear_screen
clear_screen()

# =============
# SORTING LISTS
# =============


'''
SORTING
------------
Lists allow you to sort them using a few different functions.

When you sort,  it is also helpful to understand that there are largely
two ways functions do what you want:
    - in-place change:
        - This alters the list itself.
    - returning a changed list:
        - This keeps the original list intact, and "returns" you a new list.

In-place sorting functions:
    - .reverse()
    - .sort()

Return sorting functions:
    - reversed()
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

# 1. REVERSE THE LIST ORDER
# reverse the order of the characters and print them out.
'''
.reverse() will reverse elements in a list in-place
'''
harry_potter_characters.reverse()
print(harry_potter_characters)

# 2. SORT THE LIST ALPHABETICALLY IN-PLACE:
# Print out the harry potter list in alphabetical order.
'''
You can sort any list using .sort(). Default is either
alphabetical (when list has strings) or ascending (when using numerical data)
If you mix strings and numerical data, .sort() will throw an error.

example_list.sort()
'''

harry_potter_characters.sort()
print(harry_potter_characters)

# 3. SORT THE LIST REVERSE ALPHABETICALLY IN-PLACE
# Print out the harry potter list in alphabetical order.
'''
.sort() has a "reverse" parameter. The default value is False. You can change
it to True:

example_list.sort(reverse=True)
'''
harry_potter_characters.sort(reverse=True)
print(harry_potter_characters)

# 4. RETURN AND PRINT A NEW ALPHABETICALLY ORDERED LIST:
# Print out a new harry potter list in alphabetical order.
# print out the original harry potter list afterwards.
'''
You can use sorted() to return a new list that is sorted how you want.
This is useful if you want a sorted list, but don't want to affect the original
list:

new_list = sorted(example_list)

reversed() is the return version of .reverse()
Just like sorted() is the return version of .sort()

sorted() also has a "reverse" parameter. Feel free to experiment if you'd like.
'''
print("New list:")
new_list = sorted(harry_potter_characters)
print("Original list")
print(harry_potter_characters)


'''
ADVANCED SORTING
------------
We won't use this much if at all in this class,
but you can sort by much more complicated criteria
by using the "key" parameter in either .sort() or sorted()

Be aware that this is possible, but don't worry about it for this class
'''

# 5. SORTING BY THE NUMBER OF CHARACTERS IN EACH STRING
# This uses the len() function as the criteria for sorting.
# Uncomment it to see the result.

# harry_potter_characters.sort(key = len, reverse=True)
# print(harry_potter_characters)




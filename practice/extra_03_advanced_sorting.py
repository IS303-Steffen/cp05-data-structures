from helper_functions import clear_screen
clear_screen()

# ================
# ADVANCED SORTING
# ================

harry_potter_characters = [
    "Harry Potter", "Hermione Granger", "Ron Weasley",
    "Albus Dumbledore", "Severus Snape", "Voldemort",
    "Sirius Black", "Dobby", "Luna Lovegood", "Draco Malfoy"
]

'''
OVERVIEW
--------
We won't use this much if at all in this class,
but you can sort by much more complicated criteria
by using the "key" parameter in either .sort() or sorted(). You can even
create your own functions and use that as the criteria for sorting

Be aware that this is possible, but don't worry about it for this class
'''

# 1. SORTING BY THE NUMBER OF CHARACTERS IN EACH STRING
# This uses the len() function as the criteria for sorting.

harry_potter_characters.sort(key = len, reverse=True)
print(harry_potter_characters)


# 2. CUSTOM FUNCTION FOR SORTING
# You haven't learned how to create your own functions yet, but here's a sneak
# preview. Let's say you wanted to sort the list by the number of vowels in each
# name. You can define your own custom function using lambda. This is more
# advanced than anything you'll do in this class, but feel free to see an
# example below.

harry_potter_characters.sort(key=lambda x: sum(x.count(vowel) for vowel in ["a","e","i","o","u"]))
print(harry_potter_characters)
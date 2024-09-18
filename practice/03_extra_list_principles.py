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
# MORE LIST PRINCIPLES!
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



'''
NESTED LISTS
------------
Remember how lists store other variables inside them, each variable is an
element.

Lists themselves are variables. That means they can be elements of lists.
So you can have a list with multiple lists inside it. This is a nested list.
'''


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

# 2. CREATE A NESTED LIST
# create a list called nested_list,
# and put each of the 3 above lists inside it. Print it out after.


# 3. ACCESS AN INNER LIST
# Print out the 3rd Lord of the Rings character.
'''
Just like you access elements in a list using brackets [], because the elements
in a nested list are also lists, just use brackets again to access the inner
lists.

nested_list[0] would get you the first list inside nested_list
nested_list[0][0] would get you the first element inside the first list.
'''



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

# Print out characters to see how they are originally ordered.
# print(harry_potter_characters)

# 4. REVERSE THE LIST ORDER
# reverse the order of the characters and print them out.
'''
.reverse() will reverse elements in a list in-place
'''



# 5. SORT THE LIST ALPHABETICALLY IN-PLACE:
# Print out the harry potter list in alphabetical order.
'''
You can sort any list using .sort(). Default is either
alphabetical (when list has strings) or ascending (when using numerical data)
If you mix strings and numerical data, .sort() will throw an error.

example_list.sort()
'''



# 6. SORT THE LIST REVERSE ALPHABETICALLY IN-PLACE
# Print out the harry potter list in alphabetical order.
'''
.sort() has a "reverse" parameter. The default value is False. You can change
it to True:

example_list.sort(reverse=True)
'''



# 7. RETURN AND PRINT A NEW ALPHABETICALLY ORDERED LIST:
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



'''
ADVANCED SORTING
------------
We won't use this much if at all in this class,
but you can sort by much more complicated criteria
by using the "key" parameter in either .sort() or sorted()

Be aware that this is possible, but don't worry about it for this class
'''

# 8. SORTING BY THE NUMBER OF CHARACTERS IN EACH STRING
# This uses the len() function as the criteria for sorting.
# Uncomment it to see the result.

# harry_potter_characters.sort(key = len, reverse=True)
# print(harry_potter_characters)




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

# ========================
# DATA STRUCTURES OVERVIEW
# ========================

'''
OVERVIEW
--------
Data structures are data types that can store many variables inside of them.
Every variable in a data structure is referred to as an "element" or an "item".

This .py file is meant as a high-level overview of python's standard data
structures. There are no practice problems here, but there are in the other
files.

TERMS TO KNOW
-------------
Element:
    - An individual variable in a data structure. You can also just say item.

Immutable:
    - CAN'T be changed. Once you create it, you have to destroy it
      and recreate it if you want to change it

Mutable:
    - CAN be changed. You can update it whenever you want.


'''

'''
LISTS
-----
The most common data structure you'll use. Become familiar with it.

    - Lists use square brackets []
    - When in doubt, just use a list.
    - Mutable, so you can add to them, delete things from them,
      update stuff from them, etc.
'''
# 1. MAKE A LIST USING []:
list_example = ['first thing', 'second thing', 'third thing']

# 2. PRINT A WHOLE LIST:
print(list_example)

# 3. ACCESS INDIVIDUAL ELEMENT IN A LIST:
print(list_example[0])

# 4. ALTER INDIVIDUAL ELEMENT IN A LIST:
list_example[0] = "altered first thing"
print(list_example)

# 5. ADD ELEMENT TO A LIST:
list_example.append('fourth thing')
print(list_example)

clear_screen()

'''
TUPLES
------
Be aware of tuples, but you probably won't purposefully create one
in this class. It is good to recognize it when you see one though.

    - Tuples use parentheses ()
    - Immutable, so you once they are created they can't change. That is
      occasionally useful if you want to be sure you are referencing something
      that won't be accidentally changed somewhere else in your code.
'''

# 6. MAKING A TUPLE:
tuple_example = ('first thing', 'second thing', 'third thing')

# 7. PRINTING OUT AN ENTIRE TUPLE:
print(tuple_example)

# 8. ACCESSING A SINGLE ELEMENT IN A TUPLE:
print(tuple_example[0])

# 9. "ADDING" ELEMENT TO A TUPLE:
'''
You can't add to a tuple. Only way to get around that
is to just make a new one.
'''
new_tuple_example = tuple_example + ("fourth thing",)
print(new_tuple_example)

clear_screen()

'''
DICTIONARIES
------------
Very common. Know these. In each element, you store 2 things:
    - A key (something unique)
    - A value (any value associated with that key)

Think of it like a real dictionary. You look up the word (the key) and then
you get access to the value (the definition) associated with the key.

    - Dictionaries use curly braces and colons { : }
    - Mutable. Great for storing things and getting access to them later.
'''

# 10. CREATING A DICTIONARY:
# Using a name as the key, and an age as the value
dictionary_example = {"Heidi" : 43, "Howard" : 15, "Helga" : 27}

# 11. PRINTING A WHOLE DICTIONARY:
print(dictionary_example)

# 12. PRINTING JUST THE KEYS OF A DICTIONARY:
print("\nkeys:", dictionary_example.keys())

# 13. PRINTING JUST THE VALUES OF A DICTIONARY:
print("\nvalues:", dictionary_example.values())

# 14. PRINTING EACH KEY AND VALUE IN A LIST OF TUPLES
print("\nkeys and values:", dictionary_example.items())

# 15. ACCESSING AN INDIVIDUAL VALUE
# This is usually how you use dictionaries. You enter a key to get the value.
print(dictionary_example['Heidi'])

clear_screen()

'''
SETS
----
Be vaguely aware of these, but we won't use them in this class. You can think
of it as a dictionary without values. You would only use them to store data
where every value needs to be unique.

A primary use case if for set logic/set algebra (think venn diagrams)

    - Sets use curly braces, without colons { }
    - Mutable. 
'''


set_example1 = {"Heidi", "Howard", "Helga"}
set_example2 = {"Homer", "Heidi", "Happy"}

# 16. SET UNION (COMBINE WITH NO DUPLICATES):
print("\nunion:", set_example1 | set_example2)

# 17. SET INTERSECTION (ELEMENTS IN BOTH SETS):
print("\nintersection:", set_example1 & set_example2)

# 18. SET DIFFERENCE (ELEMENTS IN FIRST BUT NOT SECOND SET):
print("\ndifference:", set_example1 - set_example2)

# 19. SET SYMMETRIC DIFFERENCE (ELEMENTS IN ONE OR THE OTHER BUT NOT BOTH):
print("\nsymmetric difference:", set_example1 ^ set_example2)
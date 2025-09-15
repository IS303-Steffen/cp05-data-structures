from helper_functions import clear_screen
clear_screen()

# ========================
# DATA STRUCTURES OVERVIEW
# ========================

'''
OVERVIEW
--------
Data structures are data types that can store many values inside of them.
Every value in a data structure is referred to as an "element" or an "item".

This .py file is meant as a high-level overview of python's standard data
structures. There are no practice problems here, but there are in the other
files.

TERMS TO KNOW
-------------
Element:
    - An individual value in a data structure. You can also just say item.

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
# 1. MAKE A LIST USING [], change and add to it:
list_example = ['first thing', 'second thing', 'third thing']
print(list_example)
print(list_example[0])
list_example[0] = "altered first thing" # alter exisiting elements
list_example.append('fourth thing') # add to it
print(list_example) # see the changed list

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

# 2. MAKING A TUPLE:
tuple_example = ('first thing', 'second thing', 'third thing')
print(tuple_example)
# this wouldn't work, Tuples are immutable; you can't change them
# tuple_example[0] = "edited first thing"

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

# 3. CREATING A DICTIONARY:
# Using a name as the key, and an age as the value
dictionary_example = {"Heidi" : 43, "Howard" : 15, "Helga" : 27}
print(dictionary_example)
print(dictionary_example['Heidi']) # You enter a key to get the value.

clear_screen()

'''
SETS
----
Be vaguely aware of these, but we won't use them in this class. You can think
of it as a dictionary without values. You would only use them to store data
where every value needs to be unique.

A primary use case is for set logic / set algebra (think venn diagrams)

    - Sets use curly braces, without colons { }
    - Mutable. 
'''

# 4. EXAMPLES OF SETS
set_example1 = {"Heidi", "Howard", "Helga"}
set_example2 = {"Homer", "Heidi", "Happy"}

# 4.1. SET UNION (COMBINE WITH NO DUPLICATES):
print("\nunion:", set_example1 | set_example2)

# 4.2 SET INTERSECTION (ELEMENTS IN BOTH SETS):
print("\nintersection:", set_example1 & set_example2)

# 4.3 SET DIFFERENCE (ELEMENTS IN FIRST BUT NOT SECOND SET):
print("\ndifference:", set_example1 - set_example2)

# 4.4 SET SYMMETRIC DIFFERENCE (ELEMENTS IN ONE OR THE OTHER BUT NOT BOTH):
print("\nsymmetric difference:", set_example1 ^ set_example2)
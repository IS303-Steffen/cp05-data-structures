# mention the __.dict__ of classes for printing out everything a class has


# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################

'''
    Each element in a dictionary stores 2 things:
        a key (unique value, can't be repeated)
        a value (associated with the key. Can be repeated)

    So the first element is a key/value, the 2nd element is another key/value, etc.

'''

# create a dictionary using {:} that stores key/values for:
# "A": 4.0, "A-": 3.7, "B+": 3.4, "B": 3.0


# Find the value for the key of "A".
# in dictionaries, you use [] like with lists, but instead of providing an index, you provide a key



# Add an entry with B- as the key and 2.7 as the value


# modify the entry for the key "A" to be 4.01

# delete items using del, or pop(key)
# try deleting B-
#
# or use pop:

# delete everything with .clear():
#grade_dict.clear()

#######
# .get()
# looks for the value of the key given.If it can't find it returns the value after the comma
# safer than just grade_dict["A"] because it handles the case of the key not existing:


# try getting the value for the key of "F". if it isn't found, return "Grade not found"


# setdefault(key, value)
# You can grab a value if it is there, or insert it if it isn't there:
# try adding F , 0.0 using setdefault. setdefault() returns the value of the key, or the new value set.


# try adding A, 5.0 with setdefault



#sometimes, you only want the keys, values, or both in a list-type format:

# use .keys() to print only the keys

# use .values() to print only the values


# use .items() to return keys and values in a tuple pair.


# also useful with if statements. It will check the key by default.
# check if B+ is a key in the grade dictionary:





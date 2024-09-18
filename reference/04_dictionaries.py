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

# ============
# DICTIONARIES
# ============

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

# 1. CREATE A DICTIONARY:
# Create a dictionary using {:} that stores key/values for:
# "A": 4.0, "A-": 3.7, "B+": 3.4, "B": 3.0
# print it out afterwards
grade_dict = {"A": 4.0, "A-": 3.7, "B+": 3.4, "B": 3.0}
print(grade_dict)

# 2. ACCESS A SPECIFIC VALUE:
# Find the value for the key of "A". Print it out.
'''
in dictionaries, you use [] like with lists,
but instead of providing an index, you provide a key

value = example_dict['key']
'''
gpa_value = grade_dict['A']  # Returns 4.0
print(gpa_value)

# 3. ADD AN ELEMENT:
# Add an element with B- as the key and 2.7 as the value
# print out the whole dictionary to see if it was added.
'''
You can add elements to dictionaries by using brackets with the new key
and the value on the right side of an equals sign.

example_dict[new_key] = new_value
'''
grade_dict['B-'] = 2.7
print(grade_dict)

# 4. MODIFY AN ELEMENT:
# modify the value for the key "A" to be 4.01
'''
You can modify something with the same syntax as adding something.
Just use an existing key.
'''
grade_dict['A'] = 4.01
print(grade_dict)

# 5. DELETING ELEMENTS:
# Delete the element with the key of "B-"
'''
You can delete using:

    del example_dict[key]

or

    example_dict.pop(key)

pop() will return the element deleted.
You can also delete everything using .clear()
'''

# using del:
#del grade_dict['B-']
# using pop:
removed_gpa = grade_dict.pop('B-')
print(removed_gpa)


# 6. GET A VALUE USING .GET():
# print out the value of "A" but use the .get() function
'''
It looks for the value of the key given. If it can't find it returns "None"
This is safer than just example_dict["A"]
because it handles the case of the key not existing:
'''
value = grade_dict.get("A")
print(value)

# 6. GET A NONEXISTANT VALUE USING .GET():
# try getting the value for the key of "F". if it isn't found,
# return "Grade not found". Print out the result of .get()
'''
You can provide a default value with .get() for when the key isn't found:

example_dict.get(key, "Value if not found")
'''

value = grade_dict.get('F', 'Grade Not Found')
print(value)


# 7. DISPLAY ONLY THE KEYS:
# Print just the keys
'''
You can use .keys() to get only the keys of a dictionary

example_dict.keys()
'''
grades = grade_dict.keys()
print(grades)

# 8. DISPLAY ONLY THE VALUES:
# Print only the values
'''
You can use .values() to get only the keys of a dictionary

example_dict.values()
'''
gpas = grade_dict.values()
print(gpas)

# 9. DISPLAY KEYS AND VALUES:
# use .items() to return keys and values in a tuple pair.
'''
You can use .items() to return keys and values in a tuple pair.

example_dict.items()
'''
grade_gpa_pairs = grade_dict.items()
print(grade_gpa_pairs)


'''
TIP
---
.keys(), .values(), and .items() will become much more useful
when we start talking about loops. 
'''

# 10. CHECK IF A KEY IS IN THE DICTIONARY:
# check if B+ is a key in the grade dictionary.
# If so, print "That is a valid grade"
'''
Using "in" is useful with if statements. It will check the key by default.
'''
if "B+" in grade_dict:
    print("That is a valid grade")




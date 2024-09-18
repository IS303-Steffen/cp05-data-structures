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

# =====
# LISTS
# =====

'''
OVERVIEW
--------
The most common data structure you'll use. Become familiar with it.

    - Lists use square brackets []
    - When in doubt, just use a list.
    - Mutable, so you can add to them, delete things from them,
      update stuff from them, etc.
'''


# 1. MAKE A LIST OF STRINGS:
# Store "Harry", "Hermione", "Ronald", "Luna" in a list:



# 2. PRINT THE WHOLE LIST:
# Print the list of the Harry Potter characters
'''
You can print the whole list, but its a little ugly.
We'll learn how to print a whole list prettier when
we get to loops in the next section.
'''


# 3. ACCESS SPECIFIC ITEMS IN THE LIST:
# Print out the 1st item in the list, and then the 3rd item.
'''
You can access specific elements of the list using brackets, and then the index
number you want, like this: example_list[2]

IMPORTANT: indexes start at 0. So the 1st element = 0, 5th element = 4, etc.
If it helps, think of it like when you are born, you are 0 until you
have moved 1 year through life. So during your 1st year you are 0 years old.
'''



# 4. ACCESS AN ELEMENT ON THE LIST THAT DOESN'T EXIST:
# Put in an index that doesn't exist. This will throw an error, but it is 
# good to become familiar with common errors. Comment out this code afterwards.



# 5. GET THE LENGTH OF A LIST:
# Print out how many ELEMENTS are in your list (the length)
'''
the len() function will tell you how many elements are in a list (or any other
data structure). It also works on strings.
'''


# 6. ADD AN ELEMENT TO THE END OF A LIST:
# Add "Dumbledore" to your list.
'''
Use .append(item) to add something to the end of your list:

example_list.append("Thing you want to add")
'''


# 7. ADD ELEMENTS AT THE BEGINNING AND MIDDLE OF YOUR LIST:
# Add "Fred" to the beginning of the list. Add "George" to the 3rd position
'''
You can use .insert(item, index) to insert a new element
at the index you specify:

example_list.insert("Thing to add", 2)
'''



# 8. DELETE ELEMENTS FROM YOUR LIST:
# Delete the last thing in your list
'''
you can delete something from the list using .pop()
by default it gets rid of the last thing on the list:

example_list.pop()
'''



# 9. SAVE THE THING YOU POPPED:
# Pop the 4th item in your list, but save it in a variable using .pop()
# print out your whole list, and then print out the item you popped.
'''
You can give pop() an index argument to delete something other than the last
thing. pop() is also cool because it give you the thing its deleting to store
if you want. The technical term is it is "returning" the variable to you.

popped_variable = example_list.pop(1)
'''


# 10. CHECK IF VALUE IS IN YOUR LIST:
# Check if "Harry" is in your list. Print out a message if so.
'''
You can use "in" with lists to check what is in or not in them:

if "example" in example_list:
    print("Found it")

'''


# 11. CHECK IF VALUE IS NOT IN LIST:
# If Voldemort is not in the list, print "Yay"



# 12. PRINT OUT A RANGE OF ELEMENTS:
# Print out the 2nd to the 4th things in the list
'''
To get a range of elements you can specify a starting and ending index with
a colon. This is often called "slicing":

example_list[0:2]

That would get the first and second items. The range you specify is inclusive
on the lower end, and exclusive on the upper end: it gets 0, 1, but not 2 in
the example above. This makes it easy to tell how many things you're getting:
2-0 = 2 so your "slice" you're grabbing is 2 elements long.
'''


# 12. PRINT OUT THE LAST ELEMENTS:
# Print out the last thing in your list, and pretend you don't know how many
# things are in the list.
'''
To get the last element of a data structure, you can use -1 as the index.
You can also get the 2nd to last with -2, etc.
'''



'''
OTHER USEFUL LIST FUNCTIONS:
----------------------------

Lots of cool functions to use with lists.
We covered some, see the textbook for more:

append()	Add an element at the end of the list.	lstNames.append("Salsa")

clear()	    Removes all the elements from the list so that the length is now 0.
            lstNames.clear()

copy()	    Return a copy of the list so you can store it to a new variable.
            This creates a true copy so that the variables are NOT pointing to
            the same memory location. You can change one variable and it will
            not affect the other.	lstNew = lstNames.copy()

count()	    Returns the number of times a specific value is found in a list.
            print( lstNames.count("Tap"))

extend()	Add one or more items from another list to the end of the current
            list.	lstNames.extend(lstOtherNames)

index()	    Returns the numerical position for the first item that has
            a specific value.	print(lstNames.index("Tap"))

insert()	Increase the size of the list and add a new item at a specific
            position. This example would increase the length of the list by 1
            and then add the new item at the beginning of the list.
            lstNames.insert(0, "Irish Folk")

pop()	    Remove an item from the list based upon the numerical position
            (0 based). You could use the negative indexing to remove the
            last item in the list (-1).	lstNames.pop(0) #removes first item

remove()	Removes the first item in the list that has the specified value.
            It also decreased the size of the list by 1. This only removes
            the first one found. If there were two items with the same value
            only the first would be removed. You would want to use a loop if
            you needed to remove more than one.	lstNames.remove("Tap")

reverse()	Reverses the order of the list so that the last becomes the first
            and the first becomes the last.	lstNames.reverse()

sort()	    Sorts the list in ascending order based upon alphabetical or
            numerical order. If you want a descending list, you can sort the
            list and then issue a reverse(). NOTE: If you want to sort the
            list in descending order you can use the reverse parameter
            lstNames.sort(reverse=True).	lstNames.sort()
'''

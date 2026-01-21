from helper_functions import clear_screen
clear_screen()

# ================================
# IDENTITY OPERATOR AND REFERENCES
# ================================

'''
OVERVIEW
------------
One way to think about variables is that they are storing a reference to a place
in your computer's memory. Other languages call these references "pointers". 

If you are working with a mutable datatype (like lists and dictionaries) and you
"mutate" the variable (e.g. change it by appending something etc) that will
change the object in memory. Any variable that references that object in memory
then will read the changed value. You just need to be aware of this anytime
you assign something like a list or dictionary to multiple variables.
'''

list_a = [1, 2, 3]
list_b = [1, 2, 3]

# 1. == VS "is" AND id()
# Use list_a and list_b above.
# 1. Print out the result of checking if list_a and list_b are equal to each other.
# 2. Now print out the result of list_a is list_b. What is the result?
# 3. Try printing out id(list_a) and id(list_b)
print(list_a == list_b)
print(list_a is list_b)

print("IDs of each: ", id(list_a), id(list_b))

# 2. UNDERSTANDING REFERENCES
# Use the list_c below.
# 1. Check if it is equal to list_a
# 2. Check if list_c is list_a
# Check their ids. 

list_c = list_a
print(list_c == list_a)
print(list_c is list_a)
print("ids of each: ", id(list_c), id(list_a))

# 3. EDITING THE REFERENCED DATA
# Append 4 to list_c. Then print out list_a. What happened?
list_c.append(4)
print(list_a)

# 4. MAKING A COPY
# Make list_d from list_b.copy(). Now change list_d. Notice that list_b doesn't
# change

list_d = list_b.copy()
list_d.append(4)
print("doesn't change: ", list_b)


'''
NOTE: DOESN'T APPLY TO IMMUTABLE DATAYPES
'''
# # assign num_2 to equal num_1
# num_1 = 1
# num_2 = num_1

# # now change num_2. Does num_1 change?
# num_2 = 2
# print(num_1) # Nope!

'''
ints, floats, strings, booleans, are all immutable.
Every time you change the value, you are essentially destroying and recreating
a variable. So you don't have to worry about changing the value of one variable
affecting other variables you've created.
'''



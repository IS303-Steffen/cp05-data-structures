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

# Unpacking:
'''
Sometimes, you want to grab the elements in a list, and put them into
individual variables. This is called "unpacking"

you do it like this:
var1, var2, var3 = example_list

if the number of elemnts in the list doesn't match the number of variables you are trying to put things into,
it won't work. You can use [0:3], etc if you only want to grab a part of the list.
'''

# Characters from Harry Potter
harry_potter_characters = [
    "Harry Potter", "Hermione Granger", "Ron Weasley",
    "Albus Dumbledore", "Severus Snape", "Voldemort",
    "Sirius Black", "Dobby", "Luna Lovegood", "Draco Malfoy"
]

# practice:
# put the first 3 characters into 3 separate variables, then print each out.


#####
# sometimes, You may want to store a list inside of a list! #inception
####

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

# create a list called list_of_character_lists, and put each of the 3 above lists inside it:


# try printing out the 3rd Lord of the Rings character.



### basic sorting

print(harry_potter_characters)

# reverse the order of the characters using .reverse()


# you can sort any list using .sort()
# (but it should only be of comparable data types. No lists of ints and strings)



#sort_them reversed using .sort(revers=True):


# You can get much more complicated with sorting, even using custom functions to sort things on.
# Here's an example using len. We won't go into details on this or do complicated sorting in this class
# but you should be aware it is totally possible.

harry_potter_characters.sort(key = len, reverse=True)
print(harry_potter_characters)




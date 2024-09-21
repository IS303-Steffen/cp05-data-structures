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

# =====================================
# EXTRA - EXAMPLE OF SORTING ALGORITHMS
# =====================================

import random
import time
from extra_02_sorting_algorithms import bubble_sort, timsort

'''
OVERVIEW
--------
This is just a fun bonus file. If you were taking a computer science class,
you'd probably spend a significant amount of time going into sorting
algorithms and write your own custom sorting algorithms.

In IS, we care more about quickly coding up solutions to solve business
problems, so we spend a less time on writing up fundamental algorithms, like
for sorting.

This is also because the functions built into python for sorting are already
incredibly efficient. This file is referencing two sorting functions
that are in the EXTRA_02_sorting_algorithms.py file. 

One is a bubble sort, which is a classic and simple sorting algorithm.
You can see a simple visualization of it here:
    https://www.youtube.com/watch?v=9I2oOAr2okY

The other is a simplified version of a timsort, which combines two separate
sorting algorithms (insert and merge).

This file is generating a random list of 15,000 numbers and asking those two
algorithms to sort it, followed by python's built in .sort() function.
Python's built in .sort() function also uses a timsort, but the function is
using precompiled C code that came with python when you installed it. It is 
incredibly efficient. Run the code in this file and see how fast the built-in
function in python is. Its part of the reason we don't cover algorithms in more
detail. There is already such an efficiently built way to sort (and other ways
in exisitng libraries) that we want to focus more on HOW to use that to solve
problems, rather than reinventing the wheel.

'''


# Create a list of 15,000 random numbers using list comprehension
arr = [random.randint(1, 100000) for _ in range(15000)]

# Test Bubble Sort
arr_bubble = arr.copy()
start = time.perf_counter()
bubble_sort(arr_bubble)
end = time.perf_counter()
print(f"Bubble Sort took {end - start:.6f} seconds.")

# Test Timsort (mock)
arr_timsort = arr.copy()
start = time.perf_counter()
timsort(arr_timsort)
end = time.perf_counter()
print(f"Timsort (mock) took {end - start:.6f} seconds.")

# Test Python's built-in .sort()
arr_builtin = arr.copy()
start = time.perf_counter()
arr_builtin.sort()
end = time.perf_counter()
print(f"Python built-in sort() took {end - start:.6f} seconds.")

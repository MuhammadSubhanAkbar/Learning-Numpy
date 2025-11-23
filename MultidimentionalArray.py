import numpy as np

# This of this like a 0 dimensional array, think of it like a single point
array = np.array('A')
print(array)
# We can determine dimension of array as follows
print("Dimensions:",array.ndim, end="\n\n")

# We can find the shape of the array
print(array.shape, end="\n\n")

# An array with more than one item's init is known as a one array. #
# A one dimensional array contains only one list.

array = np.array(['A','B','C','D'])
print(array)

# We can determine dimension of array as follows
print("Dimensions:",array.ndim,end="\n\n")

# We can find the shape of the array
print(array.shape, end="\n\n")

# An array with more than one list is know as a 2d array.
#it is like a matrics

array = np.array([
    ['A','B','C','D'],
    ['E','F','G','H'],
    ['I','J','K','L']
])
print(array)

# We can find the shape of the array
print(array.shape, end="\n\n")

# We can determine dimension of array as follows
print("Dimensions:",array.ndim)
print()

#An array more than one 2d arrays create a 3d array

array = np.array([
    [['A','B','C','D'],['E','F','G','H'],['I','J','K','L']],
    [['A','B','C','D'],['E','F','G','H'],['I','J','K','L']],
    [['A','B','C','D'],['E','F','G','H'],['I','J','K','L']]
])

print(array)

# We can determine dimension of array as follows
print("Dimensions:",array.ndim)

# We can find the shape of the array
print(array.shape, end="\n\n")

# FIXED: Using valid indices for the 3D array with shape (3, 3, 4)
word = array[1, 2, 3]  # This selects 'L' from the second 2D array, third row, fourth column
print("Selected element:", word)

# Example of creating a word by selecting multiple elements
word = array[0, 0, 0] + array[0, 0, 1] + array[0, 0, 2]  # Creates "ABC"
print("Created word:", word)
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

# NOTE : The list of element in each list should all be the same, in a multidimensional element of the array should
#        remain the same.

#We can also select specific element from any list in each type of array, we can make a word by it.
word = array[1,3,7]

print(word)
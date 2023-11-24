import numpy as np

array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])

print(array_example.ndim)
# 3

print(array_example.shape)
# (3, 2, 4)

print(array_example.size)
# 24

print(array_example.dtype)
# int64

print(array_example.itemsize)
# 8

print(array_example.data)
# <memory at 0x7f6e0d1f0e10>

array_example2 = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]],

                           [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])

print(array_example2.ndim)
# 3

print(array_example2.shape)
# (4, 2, 4)

print(array_example2.size)
# 32

array_example3 = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]]])

print(array_example3)
print(array_example3.shape)
print(array_example3.ndim)
# 3



# Crear un array de 4 dimensiones
array_4d = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]])

print(array_4d)
# [[[[ 1  2]
#    [ 3  4]]
#  [[ 5  6]
#    [ 7  8]]]
#     [[[ 9 10]
#    [11 12]]
#  [[13 14]
#    [15 16]]]]

print(array_4d.shape)
# (2, 2, 2, 2)
print(array_4d.ndim)
# 4

# Crear un array de 5 dimensiones
array_5d = np.array([[[[[1, 2], [3, 4]], [[5, 6], [7, 8]]], [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]]])
print(array_5d)


#reshape
example_reshape = np.arange(64).reshape(2, 4, 8)
print(example_reshape)

example_reshape2 = np.arange(64).reshape(4, 4, 4)
print(example_reshape2)

print()
print()
example_reshape3 = np.arange(64).reshape(2, 2, 4, 4)
print(example_reshape3)


#operaciones con matrices

#suma
array_operation1 = np.array([1, 2, 3])
array_operation2 = np.array([10, 11, 12])

print(array_operation1 + array_operation2)
print()

#matrix product
print(array_operation1 @ array_operation2)
new_array = array_operation1.dot(array_operation2)
print(new_array)

array_operation3 = np.array([[1, 2], [3, 4]])
array_operation4 = np.array([[5, 6], [7, 8]])
new_array2 = array_operation3.dot(array_operation4)
print(new_array2)




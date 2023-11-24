import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])

cero = np.zeros(10)
print(cero)
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

unos = np.ones(10)
print(unos)
# [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

em = np.empty(10)
print(em)
# [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

rang = np.arange(10)
print(rang)
# [0 1 2 3 4 5 6 7 8 9]

rang2 = np.arange(3, 10)
print(rang2)
# [3 4 5 6 7 8 9]

rang3 = np.arange(3, 10, 2)
print(rang3)
# [3 5 7 9]

lin = np.linspace(0, 10, 5)
print(lin)
# [ 0. ,  2.5,  5.,   7.5, 10. ]

x = np.ones(2, dtype=np.int64)
print(x)
# [1 1]

#Agregar y ordenar elementos

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])

order = np.sort(arr)
print(order)
# [1 2 3 4 5 6 7 8]

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

cadena = np.concatenate((arr1, arr2))
print(cadena)
# [ 1  2  3  4  5  6  7  8  9 10]

arrx = np.array([[1, 2], [3, 4]])
arry = np.array([[5, 6]])

cadena2 = np.concatenate((arrx, arry), axis=0)
print(cadena2)
# [[1 2]
#  [3 4]
#  [5 6]]

cadena3 = np.concatenate((arrx, arry.T), axis=1)
print(cadena3)
# [[1 2 5]
#  [3 4 6]]

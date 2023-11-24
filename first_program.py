import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(a[2:6])
# [3 4 5 6]

print(a[2:])
# [3 4 5 6 7 8]

print(a[:6])
# [1 2 3 4 5 6]

print(a[:])
# [1 2 3 4 5 6 7 8]

print(a[-1])
# 8

print(a[-3])
# 6

print(a[-3:])
# [6 7 8]

print(a[:-3])
# [1 2 3 4 5]

print(a[2:6:2])
# [3 5] 2 is the step

print(a[::2])
# [1 3 5 7] 2 is the step

print(a[::-1])
# [8 7 6 5 4 3 2 1] -1 is the step

print(a[5:1:-1])
# [6 5 4 3] -1 is the step

print(a[5:1:-2])
# [6 4] -2 is the step

print(a[5::-2])
# [6 4 2] -2 is the step

print(a[:5:-2])
# [8 6] -2 is the step

print(a[:5:2])
# [1 3 5] 2 is the step
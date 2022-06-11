#	В матрице найти номер строки, сумма чисел в которой максимальна.
import random
import numpy as np
C = 10
R = 5
a = []
for i in range(R):
    b = []
    for j in range(C):
        b.append(random.randint(0, 9))
        print("%3d" % b[j], end='')
    a.append(b)
    print()

for i in range(C):
    print(" --", end='')
print()

max_sum = 0
row = 0
for j in range(R):
    s = 0
    for i in range(C):
        s += a[j][i]
        print("%3d" % s, end='')
        if s > max_sum:
            max_sum = s
            row = j
    print()
print(row + 1)


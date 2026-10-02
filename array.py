import numpy as np

a = np.linspace(0, 9, 10, dtype=int)
print(a)

b = a.copy()
b[b % 2 != 0] = -1
print(b)

c = a.reshape(2, 5)
print(c)

s = 0
for x in a:
    if x % 2 == 0:
        s += x
print(s)
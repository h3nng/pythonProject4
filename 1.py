import numpy as np
a = np.arange(5)
print(a)
b = a[0:1]
c = a[0]
a[0] = 10
print(id(b))
print(id(c))

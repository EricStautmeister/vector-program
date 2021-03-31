import math
import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi)
array = ([1, 2, 2],
         [2, 3, 4],
         [5, 5, 5],
         [100, 100, 100])

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
for i in array:
    print(i)
    x = i[0]
    y = i[1]
    z = i[2]
    ax.scatter(x, y, z)

plt.show()

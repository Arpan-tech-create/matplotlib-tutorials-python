
import numpy as np

import matplotlib.pyplot as plt

x=np.array([23,12,43,2])
y=np.array([77,12,33,21])

plt.plot(x,y,marker='o')

plt.xlabel("First person")
plt.ylabel("Marks")
plt.show()
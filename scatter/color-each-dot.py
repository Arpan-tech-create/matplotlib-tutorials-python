
from matplotlib import colors
import numpy as np

import matplotlib.pyplot as plt

x=np.array([23,12,43,2,55,12,78,90,100])
y=np.array([77,12,33,21,44,223,67,12,46])

colors=np.array(["red",'green','blue','orange','pink','purple','black','cyan','yellow'])

plt.scatter(x,y,c=colors,cmap='viridis')

plt.colorbar()
plt.show()
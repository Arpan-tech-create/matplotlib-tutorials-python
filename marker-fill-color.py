from matplotlib import markers
import numpy as np

import matplotlib.pyplot as plt

x=np.array([44,23,1,5])
y=np.array([77,12,33,21])

plt.plot(x,y,'o:',ms=10,mec='r',mfc='b')
plt.show()
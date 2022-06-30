import numpy as np
import matplotlib.pyplot as plt

x=np.array(["A","B","C","D"])
y=np.array([12,50,44,20])

plt.barh(x,y,height=0.1)
plt.show()
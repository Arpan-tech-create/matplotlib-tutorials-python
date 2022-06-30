
import numpy as np

import matplotlib.pyplot as plt

x=np.array([23,12,43,2])
y=np.array([77,12,33,21])

font1={'family' : 'sans-serif','color':'blue','size':'15'}
font2={'family' : 'serif','color':'red','size':'15'}
plt.plot(x,y,marker='o')

plt.title("Student analysis",fontdict=font1)

plt.xlabel("First person",fontdict=font2)
plt.ylabel("Marks",fontdict=font2)
plt.grid(axis='y')
plt.show()
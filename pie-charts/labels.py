import matplotlib.pyplot as plt
import numpy as np

a=np.array([44,12,33,15])
l=["Arpan","Bhoi",'Patel','Parmar']

plt.pie(a,labels=l)
plt.show()
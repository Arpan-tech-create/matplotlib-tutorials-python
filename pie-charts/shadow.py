import matplotlib.pyplot as plt
import numpy as np

a=np.array([44,12,33,15])
l=["Arpan","Bhoi",'Patel','Parmar']
e=[0.2,0.1,0,0]

plt.pie(a,labels=l,explode=e,shadow=True)
plt.show()
import numpy as np
import matplotlib.pyplot as plt
x = np.array([10,20,30,40,50])
y= np.array([80,60,40,20,0])
x.shape == y.shape 

fig,ax = plt.subplots(figsize=(14,8))
ax.plot(x,y,'r-')
plt.axvline(x=30,ymin=0, ymax=0.30)
plt.axhline(y=40, xmin=0,xmax=0.50)
ax.set_title("Example of Demand Curve", fontsize=24)
ax.set_xlabel("Quantity Demanded", fontsize=18)
ax.set_ylabel("Price", fontsize=18)
plt.show()

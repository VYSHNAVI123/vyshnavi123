from matplotlib import pyplot as plt
import numpy as np
x=np.arange(0,10,1)
k=1
a=0
l=[]
for i in range(0,10,1):
	for j in range(0,k,1):
		a=a+1
	l.append(a)
plt.stem(x,l)
plt.show()
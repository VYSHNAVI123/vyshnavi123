import matplotlib.pyplot as plt;
import numpy as np;
f1=int(input("enter the frequency"));
fs=int(input("enter the sample frequency"));
n=int(input("enter the no of samples"));
t=np.arange(n)
y=np.sin(2*np.pi*t*f1/fs)
plt.xlabel('time period')
plt.ylabel('amplitude')
plt.subplot(3,1,3)
plt.stem(t,y)
plt.show()



import numpy as np

import matplotlib.pyplot as plot
a=int(input("enter length of x[n]:"))
b=int(input("enter length of h[n]:"))
x=np.arange(a)
for i in range (0,a):
  x[i]=int(input())
h=np.arange(b)
for i in range (0,b):
  h[i]=int(input())
y=np.arange(a+a-1)
for n in range(0,a+b-1):
   s=0
   for k in range(0,a):
      if(n-k>=0 and n-k<b):
         s=s+x[k]*h[n-k]
   y[n]=s
print(y)

import numpy as np 
import matplotlib.pyplot as plt
s=float(input("enter the value s:"))
p=float(input("enter the value p:"))
wp=float(input("enter the value wp:"))
ws=float(input("enter the value ws:"))
a=float(1/(p**2)-1)
print(a)
e=np.sqrt(a)
b=float(1/(s**2)-1)
print(b)
f=np.sqrt(b)
g=ws/wp
c=(1/e)
d=np.arccos(c*f)
h=np.arccos(g)
N=d/h
print('order of N')
w=np.arange(0,100,10)
s=np.arccos(w/wp)*N
k=e**2
p=k*((np.cos(s))**2)
l=k*((np.cosh(s))**2)
q=1/(np.sqrt(1+p))
m=1/np.sqrt(1+l)
if(w<wp):
	print(q)
plt.plot(w,q)
else:
	print(m)
plt.plot(w,m)
plt.show( )

import random
r1=input("enter the no of rows in 1st matrix")
c1=input("enter the no of columns in first matrix")
a=[[random for col in range(c1)]for row in range(r1)]
for i in range(r1):
	for j in range(c1):
		a[i][j]=input()
r2=input("enter the no of rows in 2nd matrix")
c2=input("enter the no of columns for 2nd matrix")
b=[[random for col in range(c1)]for row in range(r2)]
for i in range(r2):
	for j in range(c2):
		b[i][j]=input()
d=[[random for col in range(c2)]for row in range(r1)]
if(c1==r2):
	for i in range(r1):
		for j in range(c2):
			d[i][j]=0
	for k in range(c1):
		d[i][j]+=a[i][k]*b[k][j]
		print d[i][j]
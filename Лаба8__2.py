import numpy as np 
from array import*
a=(input("Введіть цілі цифри через пробіл"))
b=(input("Введіть цілі цифри через пробіл"))
n=(input("Введіть цілі цифри через пробіл"))
s=a.split(' ')    
h=b.split(' ')
k=n.split(' ')
for i,v in enumerate(s):
  s[i]=int(v)
z=np.array([s, h, k],dtype=int )
sum=0
for i in range(3):
 for j in range(3):
  if (i+j)%2 != 0:
    sum += z[i][j]

print(sum)
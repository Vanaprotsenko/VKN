from array import *
import random
import numpy as np
mas=array('i',[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
arr = array('i',[])
for i in range(10):
 arr.append(random.randint(0,15))
s=np.sort(arr)
print(s)
arr.reverse()
print(arr)

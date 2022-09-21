import math 
x=float(input("Введіть x "))
b=math.cos(x)+math.sin(x*2)
s=pow(4,2*x)
d=math.log1p(x+1)
s1=(b/s)-d
print(s1)

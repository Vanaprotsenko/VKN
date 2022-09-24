import math
a=float(input("Введіть нижнью межу табулювання  "))
b=float(input("Введіть верхню межу табулювання "))
h=float(input("Введіть крок табулювання "))
s=[]
def f(x):
    z=math.pow(x,1/3) + math.fabs(math.sin(x))
    return(z)
for i in range(100):
        y=f(a)
        a=round(a,2)
        y=round(y,2)
        s.append(y)
        a=a+h
        if a>b:
            break
r=min(s)
ind1=s.index(r)
print(s)
print("Найменьше значення у списку це:",r,)
    
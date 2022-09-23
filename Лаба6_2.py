import math
a=float(input("Введіть нижнью межу табулювання  "))
b=float(input("Введіть верхню межу табулювання "))
h=float(input("Введіть крок табулювання "))
n=1
def f(x):
    z=math.pow(x,1/3) + math.fabs(math.sin(x))
    return(z)
while a<b:
    y=f(a)
    a=round(a,2)
    y=round(a,4)
    print(n,'   ',a,'   ',y)
    a=a+h
    n=1+n

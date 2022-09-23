import math
a=float(input("Введіть нижнью межу табулювання  "))
b=float(input("Введіть верхню межу табулювання "))
c=float(input("Введіть крок табулювання "))
def f(x):
    z=math.pow(x,1/3) + math.fabs(math.sin(x))
    return(z)
for i in range(100):
    y=f(a)
    a=round(a,1)
    print(i,'  ',a,'   '  ,y )
    a=a+c
    if a>b:
     break

   



     
     


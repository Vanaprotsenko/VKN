import math
def s1(x1,y1):
    l1=math.sqrt(x1**2+y1**2)
    return l1

def s2(x2,y2):
    l1=math.sqrt(x2**2+y2**2)
    return l1

def s3(x3,y3):
    l1=math.sqrt(x3**2+y3**2)
    return l1

x=float(input("Введіть координату A x:"))
y=float(input("Введіть координату A y:"))
w=float(input("Введіть координату B x:"))
a=float(input("Введіть координату B y:"))
q=float(input("Введіть координату C x:"))
z=float(input("Введіть координату C y:"))

b=str("Це координата А")
v=str("Це координата B")
n=str("Це координата C")

if(s1(x,y)>s2(w,a)) and (s1>s3(q,z)):
    print(b)
elif(s1==s2) and (s1==s3):
    print("Воні рівні ")
elif(s2(w,a)>s1(x,y)) and (s2(w,a)>s3(q,z)):
    print(v)
elif(s2==s1) and (s2==s3):
    print("Воні рівні ")
elif(s3(q,z)>s1(x,y)) and(s3(q,z)>s2(w,a)):
    print(n)
elif(s3==s1) and (s3==s2):
    print("Воні рівні")


    




      
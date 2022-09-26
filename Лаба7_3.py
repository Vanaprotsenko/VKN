import random 
a=str("+999")
first=''
second=''
third=''
f=''
for i in range(5):
    first=random.randint(100,999)
    second=random.randint(100,999)
    third=random.randint(1,99)
    f=random.randint(1,99)
    c=str(first)
    b=str(second)
    u=str(third)
    d=str(f)
    n='-'+c+'-'+b+'-'+u+'-'+d
    print(a,n)





a=input("Ведіть строку :")
s=a.split(" ")
for i in s:
    if i.istitle()==False:
        s.remove(i)
print(s)



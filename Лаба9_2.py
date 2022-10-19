A={5,"a",",","/",}
s=list(A)
print(s)
n=0
s1=[]
for e in s:
  e=str(e)
  s1.append(e)
E=set()
B=set()
r=set()
while n<len(s1):
  if not s1[n].isdigit() and not s1[n].isalpha():
    E.add(s1[n])
  elif s1[n].isdigit():
    B.add(s1[n])
  elif s1[n].isalpha():
    r.add(s1[n])
  n=n+1
print(E)
print(B)
print(r)
  
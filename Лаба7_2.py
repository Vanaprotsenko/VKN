import random
a=input("Введи слова")
s = a.split(" ")
s1 = []
for i in range(len(s)):
    z = random.choice(s)
    print(z)
    s1.append(z)
    s.remove(z)
print(s1)


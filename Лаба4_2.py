import math
x = int(input("Введіть трьохзначне число"))
last = x//100
first = x%10
second = (x-last*100-first)/10
print(first*100+second*10+last)

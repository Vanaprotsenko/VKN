import sys 
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
k = int(sys.argv[4])
a1 = a*k
b1 = b*k
c1 = c*k
V = a1*b1*c1
S = a1*b1 + b1*c1 + a1*c1
S = 2*S
print("Сторони подібного паралеллепіпеда: ", a1, b1,c1)
print("Об'єм: ", V)
print("Площа: ", S) 
import math  
x=float(input("Введіть значення х"))
if x>1:
     z=math.log10(math.fabs(x+1))+2.9*math.e*pow(math.e,0.1*x)
     print(z)
elif x>-1.1 and x<=1:
     z=(math.fabs(x)*pow(x,1/2)+(math.pow(x,1/3)-math.sin(x)))
     print(z)
elif x<=-1.1:
     z=(4*x)+(math.e*pow(math.e,x)-4*(math.fabs(x)*pow(x,1/2)))
     print(z)


   



     
     


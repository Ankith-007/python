import math as m
a=int(input("enter a value"))
b=int(input("enter b value"))
c=int(input("enter c value"))
d=b*b-4*a*c

r1=(-b+m.sqrt(d))/(2*a)
r2=(-b-m.sqrt(d))/(2*a)

print(r1)
print(r2)
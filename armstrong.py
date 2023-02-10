n = int(input("Enter a 3 digit number:"))
t = n
temp = n
digits = 0
while temp != 0 :
    digits = digits + 1
    temp = temp//10
num = 0
while t != 0 :
    rem = t % 10
    num += rem**digits
    t = t//10
if num == n :
    print("Armstrong number")
else :
    print("Not an armstrong number")
n = int(input("Enter how many fibonacci numbers you want?"))
if n == 1:
    print("0")
elif n == 0 :
    print("n cannot be zero")
elif n == 2 :
    print("0,1")
else :
    x,y = 0,1
    t = n-2
    print(0)
    print(1)
    while t > 0 : 
        z = x+y
        print(z)
        x = y
        y = z
        t = t-1
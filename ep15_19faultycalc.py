x = int(input("Enter first Number"))
print("press + for Addition")
print("press - for subtraction")
print("press * for Multiplication")
print("press / for Division")
a = input()
y = int(input("Enter second Number"))
if a =="+":
    if x == 2 and y == 3:
        print(100)
    else:
        print(x+y)
elif a=="-":
    print(x-y)
elif a=="*":
    if x== 2 and y==2:
        print(100)
    else:
        print(x*y)
elif a=="/":
    if x=="2" and y==2:
        print(100)
    else:
        print(x/y)
a=int(input("Enter first number\n"))
b=int(input("Enter second number\n"))
c=int(input("Enter third number\n"))
if a==b==c:
    print("All the numbers are equal")
elif a==b:
    if c>a:
        print(f"{c} is greatest")
    else:
        print(f"{a} and {b} are equal")
elif b==c:
    if a>b:
        print(f"{a} is greatest")
    else:
        print(f"{b} and {c} are equal")
elif a==c:
    if b>a:
        print(f"{b} is greatest")
    else:
        print(f"{a} and {c} are equal")

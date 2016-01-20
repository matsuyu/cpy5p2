#Validating triangles and computing perimeter
a=int(input("Enter side 1:"))
b=int(input("Enter side 2:"))
c=int(input("Enter side 3:"))
if a<=b<=c or b<=a<=c:
    if a+b>c:
        print("Perimeter =",a+b+c)
    else:
        print("Invalid triangle!")
elif a<=c<=b or c<=a<=b:
    if a+c>b:
        print("Perimeter =",a+b+c)
    else:
        print("Invalid triangle!")
elif b<=c<=a or c<=b<=a:
    if c+b>a:
        print("Perimeter =",a+b+c)
    else:
        print("Invalid triangle!")

#Computing the greatest common divisor
n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
if n1>n2:
    i=n1-n2
elif n2>n1:
    i=n2-n1
else:
    i=n1
while n1%i!=0 or n2%i!=0:
    i=i-1
print("The greatest common divisor:",i)

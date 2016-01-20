#Finding the factors of an integer
n=int(input("Enter the integer:"))
while n>2:
    i=2
    while n%i!=0:
        i=i+1
    print(i,end=" ")
    n=n//i
        

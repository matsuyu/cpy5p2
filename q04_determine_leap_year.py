#Determining leap year
a=int(input("Enter year:"))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print("Leap")
        else:
            print("Non-Leap")
    else:
        print("Leap")
else:
    print("Non-Leap")

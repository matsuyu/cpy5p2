#Finding the number of days in a month
month=int(input("Enter month:"))
year=int(input("Enter year:"))
if month<=7 and month!=2:
    if month%2==1:
        print(31)
    else:
        print(30)
elif month>=8 and month!=2:
    if month%2==0:
        print(31)
    else:
        print(30)
elif month== 2:
    if (year %4 ==0):
        if (year%100==0):
            if (year%400==0):
                print(29)
            else:
                print(28)
        else:
            print(29)
    else:
        print(28)
    

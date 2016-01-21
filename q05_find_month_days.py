#find a month has how many days
month=int(input("Enter month:"))
years=int(input("Enter year:"))
if month==1:
    print("January {0} has 31 days".format(years))
elif month==3:
    print("March {0} has 31 days".format(years))
elif month==5:
    print("May {0} has 31 days".format(years))
elif month==7:
    print("July {0} has 31 days".format(years))
elif month==8:
    print("August {0} has 31 days".format(years))
elif month==10:
    print("October {0} has 31 days".format(years))
elif month==12:
    print("December {0} has 31 days".format(years))
elif month==4:
    print("April {0} has 30 days".format(years))
elif month==6:
    print("June {0} has 30 days".format(years))
elif month==9:
    print("September {0} has 30 days".format(years))
elif month==11:
    print("November {0} has 30 days".format(years))
elif month==2:
    if (years %4 ==0):
        if (years%100==0):
            if (years%400==0):
                print("February {0} has 29 days".format(years))
            else:
                print("February {0} has 28 days".format(years))
        else:
            print("February {0} has 29 days".format(years))
    else:
        print("February {0} has 28 days".format(years))
    

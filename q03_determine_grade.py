#Determining grade
grade= int(input("Enter Score:"))
if 70<=grade<=100:
    print("A")
elif 60<=grade<=69:
    print("B")
elif 55<=grade<=59:
    print("C")
elif 50<=grade<=54:
    print("D")
elif 45<=grade<=49:
    print("E")
elif 35<=grade<=44:
    print("S")
elif 0<=grade<=35:
    print("U")
else:
    print("Invalid! Score must be within 0 - 100.")

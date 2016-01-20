#Conversion from miles to kilometres
print("Miles Kilometers Kilometres Miles")
for i in range(1,11):
    miles=i*1.609
    kilometers=15+5*i
    print("{0:<6}""{1:<11.3f}""{2:<11}""{3:.3f}".format(i,miles,kilometers,kilometers/1.609))#"{2:<9}".format(kilometers),"{3:.3f}".format(kilometers/1.609))

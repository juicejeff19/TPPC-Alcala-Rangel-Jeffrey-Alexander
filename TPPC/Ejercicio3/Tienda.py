import time

months = {'1': 5, '2': 10, '3': 5, "4": 15, '5': 10, '6': 20, '7': 15,
          '8': 20, '9': 25, '10': 20, '11': 30, '12': 30}

print("Welcome to our sore, please, select the number of the current month")
print("1.January"+"\n"+"2.February"+"\n"+"3.March"+"\n"+"4.April"+"\n"+"5.May"+"\n"+"6.June"+"\n"+"7.July"+"\n" +
      "8.August"+"\n"+"9.September"+"\n"+"10.October"+"\n"+"11.November"+"\n"+"12.December")
mn = input()
if int(mn) < 0 or int(mn) > 12:
    print("Xd")
    exit()
else:
    print("Please, enter your total")
    total = input()
    print("Calculating...")
    time.sleep(2)
    total1 = int(total) - ((int(total)*months[mn])/100)
    print("Your total with discount is: "+str(total1))

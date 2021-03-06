print("Hello, Welcome to our shop")
print("Please, select the number of the current month")
print("1.January, "
      "2.February, "
      "3.March, "
      "4.April, "
      "5.May, "
      "6.June, "
      "7.July, "
      "8.August, "
      "9.September, "
      "10.October, "
      "11.November, "
      "12.December ")
month = int(input())
if month == 10:
    print("Congratulations, you'll be credited with a discount of 15% over the total amount of your purchase")
    print("Please, type de amount of your purchase")
    amount = int(input())
    total = amount-amount*0.15
    print("Your total is: "+str(total))
else:
    print("input the amount of your purchase")
    amount2 = input()
    print("Your total is: "+str(amount2))

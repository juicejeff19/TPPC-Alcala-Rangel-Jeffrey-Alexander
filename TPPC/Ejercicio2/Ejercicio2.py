def multiplication(number1, number2):
    for i in range(number2):
        number3 = number1*i+number1
        print("The addition number "+str(i+1)+" is: "+str(number3))


def get_numbers():
    print("Input the first number")
    number1 = int(input())
    print("input the second number")
    number2 = int(input())
    if number1<0 or number2<0:
        print("Xd")
    else:
        multiplication(number1, number2)
    return number1, number2


if __name__ == '__main__':
    get_numbers()

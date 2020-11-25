def msg(sum):
    if  sum < 50 and sum > 1:
        print(f"{sum} Is less than fifty")
    elif sum == 50:
        print("Fifty")
    elif sum > 50 and sum < 100:
        print(f"{sum} Is almost a hundred")
    elif sum == 100:
        print(f"{sum} Is spot on!")
    else:
        print(f"{sum} Missed the spot!")


def addition (num1, num2):
    return num1 + num2
def subraction (num1, num2):
    return num1 - num2
def multiplication (num1, num2):
    return num1 * num2
def division (num1, num2):
    return num1 / num2


calc = True
while calc:
    try:
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))
        operator = int(input("Good job! Now choose between the operators \n[1] +\n[2] -\n[3] *\n[4] /\n[5] Exit calculator\n:: "))
        if operator == 1:
            msg(addition(num1, num2))
        elif operator == 2:
            msg(subraction(num1, num2))
        elif operator == 3:
            msg(multiplication(num1, num2))
        elif operator == 4:
            msg(division(num1, num2))
        elif operator == 5:
            print("Closing calculator, byebye")
            calc = False
    except ValueError as err:
        print("Invalid input. Use numbers")
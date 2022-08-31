# makes a while loop for the calculator.
while True:
    # asks user for both numbers.
    first_number = int(input("Enter your first number: "))
    second_number = int(input("Enter your second number: "))
    # asks user for choice on what they want to do.
    user_choice = int(input("Choose what you want to do (1 - add, 2 - subtract, 3 - multiply, 4 - divide, 5 - exit: "))
    # switch statement for python. Switches between user choice. Note python doesn't use + it uses ,
    match int(user_choice):
        case 1:
            print(first_number, " + ", second_number, " = ", (first_number + second_number))
        case 2:
            print(first_number, " - ", second_number, " = ", (first_number - second_number))
        case 3:
            print(first_number, " * ", second_number, " = ", (first_number * second_number))
        case 4:
            print(first_number, " / ", second_number, " = ", (first_number / second_number))
    # user is given a choice to continue or to quit.
    user_exit_choice = int(input("Would you like to quit? Type in 1 to stay and 2 to quit: "))
    # if else statement to check his choice and to either continue/break.
    if user_exit_choice == 1:
        continue
    else:
        break

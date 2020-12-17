while True:
    num1=int(input("Enter 1st number "))
    num2=int(input("Enter 2nd number "))

    choice = input("Enter your choices +, -, *, / or type ''q'' to quit: ")

    if choice == "+":
        calc = num1 + num2
        print(calc)

    elif choice == "-":
        calc = num1 - num2
        print(calc)

    elif choice == "*":
        calc = num1 * num2
        print(calc)

    elif choice == "/":
        calc = num1 / num2
        print(calc)

    elif choice == "q":
        break    

    else:
        print("wrong input")

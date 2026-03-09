'''
num1=float(input("enter 1st valu:"))
num2=float(input("enter 2nd value:"))
opr=input("enetr operation:")
if opr=="+":
    print(f"addition is:{num1+num2}")
elif opr=="-":
    print(f"sub is:{num1-num2}")
elif opr=="*":
    print(f"mul is:{num1*num2}")
elif opr=="/":
    print(f"divison is:{num1/num2}")
elif opr=="//":
    print(f"floar division:{num1//num2}")
elif opr=="**":
    print(f"square is:{num1**num2}")
elif opr=="%":
    print(f"modlues is:{num1%num2}")      
else:
    print("invalid operation!")'''


while True:
    print("\n===== CALCULATOR =====")
    print("Type 'stop' anytime to exit.")

    # Step 1: Take numbers
    user_input = input("Enter numbers separated by space: ")

    if user_input.lower() == "stop":
        print("Calculator stopped.")
        break

    try:
        numbers = list(map(float, user_input.split()))
    except:
        print("Invalid numbers! Try again.")
        continue

    # Step 2: Show operation menu
    print("\nChoose Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")

    if choice.lower() == "stop":
        print("Calculator stopped.")
        break

    result = numbers[0]

    if choice == "1":
        for num in numbers[1:]:
            result += num
        print("Addition is:", result)

    elif choice == "2":
        for num in numbers[1:]:
            result -= num
        print("Subtraction is:", result)

    elif choice == "3":
        for num in numbers[1:]:
            result *= num
        print("Multiplication is:", result)

    elif choice == "4":
        for num in numbers[1:]:
            if num == 0:
                print("Cannot divide by zero!")
                break
            result /= num
        else:
            print(f"Division is: {result:.2f}")

    else:
        print("Invalid choice! Try again.")

def calculator(num1, num2, operator):
    match operator:
        case 1:
            return num1 + num2
        case 2:
            return num1 - num2
        case 3:
            return num1 * num2
        case 4:
            if num2 == 0:
                return "Denominator cannot be \"0\"."
            else:
                return num1 / num2 
        

while True:
    print("1. Addition (+)\n2. Substraction (-)\n3. Multiplication (*)\n4. Division (/)\n5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        print("Exiting..")
        break
    elif choice > 5 or choice < 1:
        print("Invalid choice.\n")
        print("***********************\n")
        continue
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    print(f"{calculator(num1, num2, choice)}\n")

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
                print("Denominator cannot be \"0\".")
            else:
                return num1 / num2 
        case _:
            return "Invalid chocice"
        
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

print("1. Addition (+)\n2. Substraction (-)\n3. Multiplication (*)\n4. Division (/)")
operator = int(input("Enter your choice: \n"))

print(calculator(num1, num2, operator))
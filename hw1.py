name = input("Enter your name: ")
age = input("Enter your age: ")
birth_year = input("Enter your birth year: ")

print(f"Hello {name}! You are {age} years old and you were born in {birth_year}")

# *****************************************************************************************

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

print(f"Sum of the numbers: {num1 + num2}\nDifference of the numbers: {num1 - num2 if num1 - num2 > 0 else num2 - num1}\nMultipication of the numbers: {num1 * num2}\nDivison of the numbers: {num1 / num2}")
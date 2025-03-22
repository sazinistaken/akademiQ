def calculator(x, y):
    print(f"Sum: {x + y}")
    print(f"Difference: {x - y if x -y > 0 else y - x}")
    print(f"Product: {x * y}")
    if y != 0:
        print(f"Division: {x / y}")
    else:
        print("Cannot divide by zero.")

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
calculator(num1, num2)

# ****************************************************************

def isPolindrome(word):
    # reversed_word = ''.join(reversed(word))
    if word == word[::-1]:
        return True
    else:
        return False
    
string = input("Enter a word: ").lower()

if isPolindrome(string):
    print(f"{string} is a polindrome word.")
else:
    print(f"{string} is not a polindrome word.")

# ****************************************************************

def hundreadYearsOld(age):
    return 100 - age

age = int(input("Enter your age: "))
print(f"{hundreadYearsOld(age)} years left to be 100 years old.")
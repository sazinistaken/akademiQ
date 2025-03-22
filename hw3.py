for i in range(1, 101):
    print(i)
print("*******************************************")
for i in range(1, 101):
    if i % 2 == 0:
        print(i)
    #print(f"{i if i % 2 == 0 else ''}")

# ****************************************************

num = int(input("Enter a number: "))
def factorial(number):
    if number < 1:
        return 1
    else:
        return number * factorial(number - 1)
     
print(f"{num}! is {factorial(num)}")

# ****************************************************
def isPrime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    
    return True

for i in range (1, 101):
    if isPrime(i):
        print(i)

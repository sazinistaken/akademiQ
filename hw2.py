num = int(input("Enter a number: "))
print(f"{num} is {'even.' if num % 2 == 0 else 'odd.'}")

# *******************************************************

score = int(input("Enter your score: "))
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score <= 89:
    grade = 'B'
elif 70 <= score <= 79:
    grade = 'C'
elif 60 <= score <= 69:
    grade = 'D'
else:
    grade = 'F'
print(f"Your grade is: {grade}")

# *******************************************************

age = int(input("Enter your age: ")) 
if age >= 0 and age <= 12:
   age_group = "Kid"
elif age >= 13 and age <= 19:
    age_group = "Teen"
elif age >= 20 and age <= 59:
    age_group = "Adult"
else:
    age_group = "Elder"

print(f"Your age group is {age_group}.")
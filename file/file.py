data = input("Your Input: ")

with open("content.txt", "w") as file:
    file.write(data)

with open("content.txt", "r") as file:
    content = file.read()
    print(content)

name = input("What is your name? ")
midname = input("What is your middle name? ")
lastname = input("What is your last name? ")
job = input("What is your job? ")
number = input("Enter your phone numer: ")

infos = [name, midname, lastname, job, number]

with open("infos.txt", "w") as file:
    for info in infos:
        file.write(info + "\n")

with open("infos.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())
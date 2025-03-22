list = []
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    list.append(num)

max = max(list)
min = min(list)
avg = sum(list) / len(list)

print("List: ", list)
print("Maximum: ", max)
print("Minimum: ", min)
print("Average: ", avg)

# ***************************************************************
words = []
for i in range(5):
    word = input(f"Enter word {i + 1}: ")
    words.append(word)

print("List: ", words)
words.reverse()
# reversed_words = words[::-1]
# print("Reversed list: ", reversed_words)
print("Reversed list: ", words)

# **************************************************************

sample_list = [1, 2, 3, 2, 4, 5, 5, 2, 1, 3, 1, 6]
arranged_list = []

# list comprehension
#[arranged_list.append(item) for item in sample_list if item not in arranged_list]

for item in sample_list:
    if item not in arranged_list:
        arranged_list.append(item)


print("List before arrange: ", sample_list)
print("List after arrange: ", arranged_list)



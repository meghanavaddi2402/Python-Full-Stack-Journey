# Student Marks Manager
marks = []
# Accept three marks using a loop
for i in range(3):
    mark = int(input(f"Enter mark: "))
    marks.append(mark)
print(f"Original marks: {marks}")
# Insert 90 at the beginning
marks.insert(0, 90)
# Add 75 and 85 using extend()
marks.extend([75, 85])
print(f"After adding 90, 75 and 85: {marks}")
# Check for 75 and remove it
if 75 in marks:
    marks.remove(75)
    print(f"75 was removed from the list.")
# Remove the final mark using pop()
removed_mark = marks.pop()
print(f"Final mark removed using pop(): {removed_mark}")
# Display final list and length
print(f"Final marks list: {marks}")
print(f"Number of marks: {len(marks)}\n")
print('='*20"\n")




# Number List Analyser
numbers = [20, 10, 30, 20, 40, 20]
# Sort in ascending order
numbers.sort()
print(f"Ascending order: {numbers}")
# Reverse to descending order
numbers.reverse()
print(f"Descending order: {numbers}")
# Ask the user for a number
search_num = int(input("Enter a number to search: "))
# Check whether the number exists
if search_num in numbers:
    count = numbers.count(search_num)
    index = numbers.index(search_num)

    print(f"Number {search_num} found!")
    print(f"Count: {count}")
    print(f"First index: {index}")
else:
    print(f"Number {search_num} not found.")
#summary
print(f"Smallest value: {min(numbers)}")
print(f"Largest value: {max(numbers)}")
print(f"Total: {sum(numbers)}")

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
print("="*20)




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

# Even and Odd Number Separator
numbers = [10,15,20,25,30,35]
# creating 2 empty lists
even = []
odd = []
for num in numbers:
    # Even condition
    if num % 2 == 0:
        even.append(num)#appending even numbers
    #Odd condition
    else:
        odd.append(num)#appending odd numbers
print(f"Even Numbers List:{even}")
print(f"Even Numbers List:{odd}")
# Slicing
print(f"First three values: {numbers[:3]}")
print(f"Last three values: {numbers[-3:]}")
# Backup using copy
copy_numbers = numbers.copy()
# Empting original list
cleared_list = numbers.clear()
print(f"Back up  of the original list: {copy_numbers}")
print(f"Original List:{numbers}")

# Unique Name Manager
names = ["Ashu","Rahul","Asha","Jhon","Rahul"]
converted_list = set(names)
#checking types
#print(type(names))
#print(type(converted_list))
print(f"Original names: {converted_list}")
# adding 
converted_list.add("Meera")
print(f"List after adding a name using add: {converted_list}")
#updating
converted_list.update(("Arun","Priya"))
print(f"List after adding a name using update: {converted_list}")
# Checking and removing Jhon
if "Jhon" in converted_list:
    converted_list.remove("Jhon")
print(f"list after removing jhon: {converted_list}")
#  using discard()
converted_list.discard("David")
print(f"list after discarding david: {converted_list}")
# using loop to display unique name
for name in converted_list:
    print(name)

# Course Student Comparison

python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"}

# Students from both courses
both_courses = python_students.union(da_students)
# Students learning both courses
common_students = python_students.intersection(da_students)
# Students learning only Python
only_python = python_students.difference(da_students)
# Students learning only one course
only_one = python_students.symmetric_difference(only_python)
# Check if DA is a subset of Python
is_subset = da_students.issubset(python_students)
# Check if Python is a superset of DA
is_superset = python_students.issuperset(da_students)
# Check if both sets are disjoint
is_disjoint = python_students.isdisjoint(da_students)

# Display results using loops

print("Students from both courses:")
for student in both_courses:
    print(student)

print("\nStudents learning both courses:")
for student in common_students:
    print(student)

print("\nStudents learning only Python:")
for student in only_python:
    print(student)

print("\nStudents learning only one course:")
for student in only_one:
    print(student)

print(f"\nIs DA a subset of Python? {is_subset}")
print(f"Is Python a superset of DA? {is_superset}")
print(f"Are Python and DA disjoint? {is_disjoint}")





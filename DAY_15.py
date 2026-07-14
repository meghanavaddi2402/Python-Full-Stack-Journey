'''

                        #CODES


# Remove duplicate numbers
nums_ = list(map(int, input().split()))
empty_  = []

def removes_(nums_, empty_):
    for i in nums_:
        if i not in empty_:
            empty_.append(i)
    print(empty_)
removes_(nums_, empty_)

#Prime

num = int(input())
count_ = 0

def check_prime(num, count_):
    for i in range(1, num + 1):
        if num % i == 0:
            count_ += 1
    if count_ == 2:
        print("Prime")
    else:
        print("Not Prime")
        
        
check_prime(num, count_)


#Count words in sentence

str_ = input()
count_ = 0
def counting_(str_, count_):
    so_ = str_.split(' ')
    for i in so_:
        count_ += 1
    print(count_)

counting_(str_, count_)

#COUNTING CAP-SMALL LETTERS
str_ = input()
count1_ = 0
count2_ = 0
space_count = 0
def counting_(str_, count1_, count2_, space_count):
    for char in str_:
        if char.isupper():
            count1_ += 1
        elif char.islower():
            count2_ += 1
        else:
            space_count += 1
    print(f"Capital Letters {count1_}\nsmall letters {count2_}\nspace count {space_count}")
counting_(str_, count1_, count2_, space_count)


#OUTPUT
Capital Letters 7
small letters 36
space count 7

#FACTORIAL NUMBER
num_ = int(input())
def fact_(num_):
    if num_ == 0 or num_ == 1:
        return 1
    return num_ * fact_(num_ - 1)
  
print(fact_(num_))


#FIBANOCCI SERIES

num_ = int(input())

def fibb_(num_):
    if num_ <= 1:
        return num_
    return fibb_(num_ - 1) + fibb_(num_ - 2)
for i in range(num_):
    print(fibb_(i), end = " ")



'''























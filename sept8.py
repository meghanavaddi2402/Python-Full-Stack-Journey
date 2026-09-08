#control block
#BMI(Body Mass Index) use case
'''
BMI = weight/height**2
weight => kgs
height => cm

BMI chain rule
< 18.5 = underweight
18.5 to 24.9 = normal weight
25 - 29.9 overweight
>= 30 obesity

value = int(input("Enter value: "))
for i in range(value):
    weight = float(input("Enter weight in kgs: "))
    height = float(input("Enter height in mts: "))
    name = input("Enter User Name: ")
    if weight> 0 and height>0:
        bmi = (weight)/((height)**2)
        if bmi < 18.5:
            print(f"{name} is Underweight with BMI {bmi}")
        elif bmi>=18.5 and bmi<=24.9:
            print(f"{name} is Normal Weight with BMI {bmi}")
        elif bmi>25 and bmi<=29.9:
            print(f"{name} is Overweight with BMI {bmi}")
        else:
            print(f"{name} is Obse with BMI {bmi}")

    else:
        print("Enter only positive values")
'''
while True:
    try:
        weight = float(input("Enter weight in kgs: "))
        height = float(input("Enter height in mts: "))
        if weight >= 0 or height >= 0:
            break
        name = input("Enter User Name: ")
        bmi = weight / height ** 2
        if bmi < 18.5:
            print(f"{name} is Underweight with BMI {bmi:.2f}")
        elif 18.5 <= bmi <= 24.9:
            print(f"{name} is Normal Weight with BMI {bmi:.2f}")
        elif 25 <= bmi <= 29.9:
            print(f"{name} is Overweight with BMI {bmi:.2f}")
        else:
            print(f"{name} is Obese with BMI {bmi:.2f}")
        break
    except Exception as e:
        print(f"The error is: {e}")

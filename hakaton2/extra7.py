#Instructions:
# Ask the user to enter their weight in kilograms and height in meters using input().
# Calculate the Body Mass Index (BMI) using the given formula.
weight = int(input("enter weight: "))
height = float(input("enter height: "))
BMi = weight / (height * height)

if BMi<18.5:
    print("underweight")
elif 18.5<BMi<25:
    print("normal weight")
elif 25<BMi<30:
    print("overweight")
elif BMi>30:
    print("obese")
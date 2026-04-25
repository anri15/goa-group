#Instructions:
# Compare if a is greater than b and store the result in result.
#Test Cases:
#  assert result == True when a = 5, b = 3
#  assert result == False when a = 2, b = 7
a = int(input("enter first number: "))
b = int(input("enter second number: "))
if a>b:
    print("True")
elif a<b:
    print("False")

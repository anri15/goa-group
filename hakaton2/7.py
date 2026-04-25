#Instructions:
#write code that returns True if number is even, otherwise False.
#Test Cases:
#assert is_even(4) == True
#assert is_even(7) == False
#assert is_even(0) == True
number = int(input("enter your number:"))
if number %2 == 0:
    print("True")
else:
    print("False")



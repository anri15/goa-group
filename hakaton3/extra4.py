# Extra 4: Find the Maximum of Two Numbers
# Instructions:
# Write like program max_of_two(a, b) that returns the larger of the two numbers.
# Test Cases:
# assert max_of_two(3, 7) == 7
# assert max_of_two(10, 5) == 10
# assert max_of_two(-2, -5) == -2

# a = int(input('Enter first num: '))
# b = int(input('Enter second num: '))

a=3
b=7

if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print('error')
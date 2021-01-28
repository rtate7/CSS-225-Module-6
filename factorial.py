# Bob Tate
# 1/28/21
#
# Solution to Problem #6
# Obtains a user input value and then both calculates the factorial
# of that number using a for loop and determines the factorial
# using the math.factorial() function.

import math

user_input = int(input("Please enter an integer value: "))

calculated_factorial = 1
for i in range(1, user_input + 1):
    calculated_factorial *= i

factorial_from_math_module = math.factorial(user_input)

print("\nCalculated factorial:", calculated_factorial)
print("Factorial from math module:", factorial_from_math_module)


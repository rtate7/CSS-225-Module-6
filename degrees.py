# Bob Tate
# 1/28/21
#
# Solution to Problem #5
# Converts a user-inputted degree measurement to radians using 
# both a caluculation and the math.radians() function

import math

degrees = float(input("Please enter the number of degrees: "))

calculated_radians = (degrees * math.pi) / 180
library_converted_radians = math.radians(degrees)

print("\nCalculated radians:", calculated_radians)
print("Library-converted radians:", library_converted_radians)

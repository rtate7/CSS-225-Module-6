# Bob Tate
# 1/28/21
#
# Solution to Problem #3
# Uses random.choice to select a day of the week from a list and
# prints that day.

import random

days = [
    "Sunday", 
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday", 
    "Saturday"
]

print(random.choice(days))
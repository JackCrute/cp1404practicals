"""
CP1404 - Practical 4
Lists warmup
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] will return 3
# numbers[-1] will return 2
# numbers[3] will return 1
# numbers[:-1] will return all but ending 2
# numbers[3:4] will return 1 and nothing else
# 5 in numbers will return True
# 7 in numbers will return False
# "3" in numbers will return False
# numbers + [6, 5, 3] will add list elements to the end of numbers

# 1.
numbers[0] = "ten"

# 2.
numbers[-1] = 1

# 3.
print(numbers[2:])

# 4.
print(9 in numbers)

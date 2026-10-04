"""
CP1404 - Practical 3
Files
"""

# 1.

name = input("Name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2.

in_file = open("name.txt")
text = in_file.read()
print(text)
in_file.close()

# 3.

with open("numbers.txt") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    print(f"Total: {first_number + second_number}")

# 4.

total = 0
with open("numbers.txt") as in_file:
    for line in in_file:
        number = int(line)
        total += number
    print(f"Total: {total}")

"""
CP1404 - Practical 3
Files
"""

# 1.

# name = input("Name: ")
# out_file = open("name.txt", 'w')
# print(name, file=out_file)
# out_file.close()

# 2.

in_file = open("name.txt")
text = in_file.read()
print(text)
in_file.close()

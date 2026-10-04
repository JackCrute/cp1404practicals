"""
CP1404 - Practical 3
Files
"""

# 1.

name = input("Name: ")
out_file = open(name.txt, 'w')
print(name, file=out_file)
out_file.close()

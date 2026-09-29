"""
Program to calculate total price for a list of items with varying prices.

total_price = 0
get number_of_items

repeat number_of_items times
    get item_price
    total_price = total_price + item_price

if total_price > 100
    total_price = total_price * 0.90

print total_price
"""

total_price = 0
number_of_items = int(input("Number of items to buy: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items to buy: "))

for i in range(number_of_items):
    item_price = float(input("Price of item: $"))
    total_price += item_price

if total_price > 100:
    total_price *= 0.9

print(f"Total price for {number_of_items} items is ${total_price:.2f}")

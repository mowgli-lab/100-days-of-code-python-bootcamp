print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").lower()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

if size == 's':
    bill = 15
elif size == 'm':
    bill = 20
elif size == 'l':
    bill = 25

if pepperoni == 'y':
    if size == 's':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'y':
    bill += 1

print(f'Your final bill is: ${bill}.')

# # Base Prices by Size
# base_prices = {
#     's': 15,
#     'm': 20,
#     'l': 25,
# }
#
# # Pepperoni prices by size
# pepperoni_prices = {
#     's': 2,
#     'm': 3,
#     'l': 3,
# }
# # Get base price based on user input
# bill = base_prices.get(size, 0)
# # Add pepperoni if requested
# if pepperoni == 'y':
#     bill += pepperoni_prices.get(size, 0)
# # Add extra cheese if requested
# if extra_cheese == 'y':
#     bill += 1
#
# if bill > 0:
#     print(f'Your final bill is: ${bill}')
#
# else:
#     print('Invalid pizza selection')

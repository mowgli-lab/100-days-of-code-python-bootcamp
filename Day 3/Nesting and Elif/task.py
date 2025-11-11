print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input('What is your age? '))

if height >= 120:
    print("You can ride the rollercoaster")
    if age >= 18:
        print('You owe $12 dollars to ride the rollercoaster')
    elif age <= 12:
        print('You owe $5 dollars to ride the rollercoaster')
    else:
        print('You owe $7 dollars to ride the rollercoaster')
else:
    print("Sorry you have to grow taller before you can ride.")

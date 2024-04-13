print("Welcome to the roller-coaster!!")
height = float(input("Enter your height in centimeters. "))


if height >= 120:
    print("You can ride the roller-coaster!")
    age = int(input("Enter your age. "))
    if age > 18:
        print("You have to buy a 12$ ticket.")
    elif age <= 18 and age >=12:
        print("You have to buy a 7$ ticket.")
    elif age < 12:
        print("You have to buy a 5$ ticket.")
else:
    print("You have to grow taller before you ride...")
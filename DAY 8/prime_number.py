def prime_checker(number):

    for i in range(2, number + 1):
        if number % i == 0 and number == i:
            print("It's a prime number.")
        elif number % i == 0 and number != i:
            print("It's not a prime number.")
            break

num_input = int(input("Enter a number to check whether prime or not. \n"))

prime_checker(number = num_input)
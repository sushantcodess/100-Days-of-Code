import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']




print("Welcome to the PyPassword Generator!")
letters_ = int(input("How many letters would you like in your password? \n"))
symbols_ = int(input("How many symbols would you like in your password? \n"))
numbers_ = int(input("How many numbers would you like in your password? \n"))

let = []
for i in range(0, letters_):
    c = random.choice(letters)
    let += c
#   print(let)
sym = []   
for f in range(0, symbols_):
    b = random.choice(symbols)
    sym += b
num = []
for g in range(0, numbers_):
    a = random.choice(numbers)
    num += a
    
passs=(num+sym+let)
random.shuffle(passs)


# code to convert list elements into a string !
shuffled_list = ""
for x in passs:
    shuffled_list += x
print(f"Your password is {shuffled_list}")
    
    



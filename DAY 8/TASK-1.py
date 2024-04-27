import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

chosen_word_lst = [*chosen_word]
for letter in chosen_word_lst:
    if guess == chosen_word_lst:
        print("Oh Yes!")
    else:
        print(chosen_word_lst)

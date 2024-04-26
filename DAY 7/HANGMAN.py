import random
from hangman_vocabulary import word_list
from hangman_art import logo, stages


print(logo)
print("You have to guess all the letters in the word in order to win! You've got 6 lives.")
chosen_word = random.choice(word_list)

display = []

for letter in range(0, len(chosen_word)):
    display.append("_")
print(display)

lives = 6

end_of_game = False
while not end_of_game: 
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for position in range(0, len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = guess
            
    print(f"{' '.join(display)}")
    if guess not in chosen_word:
        lives = lives - 1
        print(f"You guessed {guess} and that's not in the word. You lose a life!")
        if lives == 0:
            end_of_game =True
            print("You lose!")
    if "_" not in display:
        end_of_game = True
        print("You win!")
    print(stages[lives])

print(chosen_word)




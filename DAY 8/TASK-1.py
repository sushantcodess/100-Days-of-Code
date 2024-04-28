import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

print("Welcome to HangMan!")
word_list = ["dani", "sybil", "jia", "stacy", "ariana", "valentina", "scarlit"]
chosen_word = random.choice(word_list)

#print(chosen_word)
blank = []
for letter in chosen_word:
    blank += "_"
print(blank)

lives = 6

while "_" in blank:
    guess = input("Guess a letter: ").lower()
    indi = -1
    for letter in chosen_word:
        indi += 1
        if guess == letter:
            blank[indi] = letter        
    print(blank)

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives+1])
        print(f"You lost a life! {lives} lifes remaining...")
        if lives == 0:
            print("You loose!")
            break
    if "_" not in blank:
        print("Yayy you have won!")

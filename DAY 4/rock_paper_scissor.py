import random
import icons

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors \n"))
comp_choice = random.randint(0,2)

print(f"You chose: \n {icons.options[choice]}")
print(f"Computer chose: \n {icons.options[comp_choice]}")


if choice == 0 and comp_choice == 2:
    print("You won")

elif choice > comp_choice:
    if choice == 2 and comp_choice == 0:
        print("You lose")

    else:
        print("You won")
elif choice == comp_choice:
    print("It's a draw!")
else:
    print("You lose")
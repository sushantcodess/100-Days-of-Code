print("The Love Calculator is calculating your score...")
name_1 = input("What is your name? ") 
name_2 = input("What is your partner's name? ") 

name_1 = name_1.lower()
name_2 = name_2.lower()
name1 = [*name_1]
name2 = [*name_2]

t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")
l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")

true = t+r+u+e
love = l+o+v+e

score = int(str(true) + str(love))


if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
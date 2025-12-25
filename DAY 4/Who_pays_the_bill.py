import random
no_of_friends = int(input("Enter the number of people. "))

friends_list = []
for i in range (0, no_of_friends):
    friends = input("Enter the names of your friends one at a time! ")
    friends_list.append(friends)

random_person = random.randint(0, no_of_friends - 1)
print(f"{friends_list[random_person]} has to pay the bill today :)")
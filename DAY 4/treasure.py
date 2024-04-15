line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Type the spot! ") 
position = position.lower()
alpha_position = position[0]
num_index = int(position[1]) - 1
first = ["a", "b", "c"]
alpha_index = first.index(alpha_position)
map[num_index] [alpha_index] = "X"




print(f"{line1}\n{line2}\n{line3}")
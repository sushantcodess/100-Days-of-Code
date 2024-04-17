target = int(input("Enter a number upto 1000! \n"))

if target > 1000:
  print("Number out of range!")
else:
  sum = 0
  for i in range(2, target + 1, 2):
    sum += i



print(sum)
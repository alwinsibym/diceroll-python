import random
print("DICE ROLLER \n ")
while True:
  print("To roll the dice type 7\n")
  a=int(input())
  if a==7:
      droll=random.randint(1,6)
      print(droll)
  else:
    break

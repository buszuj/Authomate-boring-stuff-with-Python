def die()
  import random
  print("Choose your die size")
  x = input()
  
  print(random.randint(1, int(x)))
  print("again? y, n?")
  again = input()
  if again == "y":
    die()
  else:
  print("Good bye! ;D")
die()

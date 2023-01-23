for row in range(9):
  for column in range(5):
    if row <= 4:
      if column <= row:
        print("*", end=" ")
    else:
      if column >= row-4:
        print("*", end=" ")
  print()
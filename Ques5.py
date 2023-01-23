character = 65
n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
  for j in range(i):
    print(chr(character), end="")
    character += 1
    if character > 90:
      character = 65
  print()
words = input("Enter a list of words separated by space: ").split()
count = {}
for a in words:
  if a in count:
    count[a] += 1
  else:
    count[a] = 1
print("Word count:", count)
positive = []
negative = []
odd = []
even = []
count = {}
for i in range(10):
  num = int(input("Enter an integer: "))
  if num > 0:
    positive.append(num)
  elif num < 0:
    negative.append(num)
  if num % 2 == 0:
    even.append(num)
  else:
    odd.append(num)
  if num in count:
    count[num] += 1
  else:
    count[num] = 1
print("Positive numbers:", *positive)
print("Negative numbers:", *negative)
print("Odd numbers:", *odd)
print("Even numbers:", *even)
print("Number count:", count)
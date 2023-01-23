start = int(input("Start of the range: "))
end = int(input("End of the range: "))
divisor = int(input("Divisor: "))
for i in range(start, end+1):
    if i % divisor == 0:
        print(i)

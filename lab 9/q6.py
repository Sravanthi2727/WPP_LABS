n = int(input("Enter a number :"))
m = 0
for i in range(1, n+1):
    m = m + (1/i)

print("Value of series 1 + 1/2 + 1/3 + ….. + 1/N :", m)
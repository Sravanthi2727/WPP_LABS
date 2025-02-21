n = int(input("Enter a number :"))
s = 0
for i in range(1, n):
    if(n%i == 0):
        s += i

if(n==s):
    print("It is a Perfect Number!")
else:
    print("It is a NOT Perfect Number!")

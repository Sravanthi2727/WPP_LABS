def po(n, p):
    if(p == 0):
        return 1
    return n * po(n, p - 1)

n = int(input("Enter a number :"))
p = int(input("Enter power:"))

print("Value :", po(n,p))
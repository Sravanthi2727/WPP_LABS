def rec(n):
    if(n==0 or n==1):
        return 1
    return n*rec(n-1)

n = int(input("Enter a number :"))
m = 1
for i in range(1, n + 1):
    m = m*i

print("Factorial of a given number {0} with recursion {1} and without recursion {2}".format(n,m,rec(n)))


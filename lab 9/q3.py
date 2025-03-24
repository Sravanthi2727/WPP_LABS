n = str(input("Enter a number :"))
c = 0

for i in n:
    if(n.isalnum()):
       c = c+ 1

print("Number of digits :", c)
p = (input("Enter a String :"))
n = str(p)
c = 0
for i in n:
    if(i=='a' or i=='e'or i=='i'or i=='o'or i=='u' or i=='A' or i=='E'or i=='I'or i=='O'or i=='U'):
        c = c + 1
    
print("Number of Vowels in the given string {0} : {1}".format(n, c))
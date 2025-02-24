# 5. Write a Python program to replace the last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

t = []
n = int(input("Enter Number of Elements you want in List :"))
for i in range(n):
    for j in range(3):
       tu = ()
       print("In tuple number", j)
       e = input("Enter Element :")
       tu = tu + (e,)
    
    t.append(tu)
print("List created : ", t)

e = int(input("Enter the number you want to replace of last element :"))

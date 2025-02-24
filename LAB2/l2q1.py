# 1. Write a Python program to sum all the items in a list.
# a. Write a Python program to multiply all the items in a list.
# b. Write a Python program to get the largest number from a list.
# c. Write a Python program to get the smallest number from a list.
l = [1,2,3,4,5]
s = sum(l)
m = 1
for i in l:
    m *= i

large = max(l)
small = min(l)

print("The Sum of all elements is :", s)
print("The Product of all elements is :", m)
print("The Maximum of all elements is :", large)
print("The Minimum of all elements is :", small)

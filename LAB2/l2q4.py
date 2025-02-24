# 4. Write a Python program to create a tuple.
# a. To create a tuple of numbers and print one item.
# b. To create a tuple with different data types.
# c. Write a Python program to add an item to a tuple.

def tu():
    t = ()
    n = int(input("Enter Number of Elements you want in Tuple :"))
    for i in range(n):
       e = input("Enter Element :")
       t = t + (e,)
    print("Tuple created : ", t)


def numtu():
    t = ()
    n = int(input("Enter Number of Elements you want in Tuple :"))
    for i in range(n):
       e = int(input("Enter Element :"))
       t = t + (e,)
    print("Tuple created : ", t)
    print("Printing the last indexed value from tuple :", t[-1])

print("Tuple creating :")
tu()
print("Tuple of Numbers and printing item :")
numtu()
print("Adding an item in tuple :")
a = input("Enter a Item to add in tuple :")
t = 1,2,3,5
print("Current tuple :", t)
print("Tuple after added item :", t + (a,))
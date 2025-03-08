def create_tuple():
    n = int(input("Enter number of elements in the tuple: "))
    t = tuple(input("Enter element: ") for _ in range(n))
    print("Tuple created:", t)

def number_tuple():
    n = int(input("Enter number of numeric elements in the tuple: "))
    t = tuple(int(input("Enter element: ")) for _ in range(n))
    print("Tuple created:", t)
    print("Printing the last indexed value from tuple:", t[-1])

print("Tuple creation:")
create_tuple()
print("\nTuple of numbers and printing an item:")
number_tuple()

print("\nAdding an item to a tuple:")
t = (1, 2, 3, 5)
new_item = input("Enter an item to add to the tuple: ")
t = t + (new_item,)
print("Tuple after adding item:", t)

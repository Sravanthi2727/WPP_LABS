def common(l1, l2):
    f = 0
    for i in l1:
        for j in l2:
            if(i == j):
                f = 1
    if(f == 1): 
        print("True")
        return True
    else:
        print("False")
        return False
    
l1 = []
l2 = []
n = int(input("Enter No.of Elements for list 1 :"))
m = int(input("Enter No.of Elements for list 2 :"))

for i in range(n):
    n1 = int(input("Enter the Element of List 1 :"))
    l1.append(n1)

for i in range(m):
    n = int(input("Enter the Element of List 2 :"))
    l2.append(n)


common(l1,l2)
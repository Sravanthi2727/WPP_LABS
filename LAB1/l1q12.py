m1 = int(input("Enter Marks of Sub 1 out of 100 :"))
m2 = int(input("Enter Marks of Sub 2 out of 100 :"))
m3 = int(input("Enter Marks of Sub 3 out of 100 :"))
m4 = int(input("Enter Marks of Sub 4 out of 100 :"))
m5 = int(input("Enter Marks of Sub 5 out of 100 :"))
p = ((m1+m2+m3+m4+m5)/500)*100
a = p/10


if a>9 and a<=10:
    print("Your Grade : AA")
elif a>8 and a<=9:
    print("Your Grade : AB")
elif a>7 and a<=8:
    print("Your Grade : BB")
elif a>6 and a<=7:
    print("Your Grade : BC")
elif a>5 and a<=6:
    print("Your Grade : CC")
elif a>4 and a<=5:
    print("Your Grade : CD")
elif a>3 and a<=4:
    print("Your Grade : DD")
elif a>2 and a<=3:
    print("Your Grade : DF")
else:
    print("Your Grade : FAIL")

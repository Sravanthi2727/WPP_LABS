# 2. Write a Python program to count the number of strings from a given list of strings. The string
# length is 2 or more and the first and last characters are the same.
# Sample List : ['abbba', 'xybdmz',’cvnhf’, 'aba', '1221']
# Expected Result : 3
c = 0
l = ['abbba', 'xybdmz','cvnhf', 'aba', '1221']
for i in l:
    if i[0] == i[-1]:
        c += 1

print("Result :", c)
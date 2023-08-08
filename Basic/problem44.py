# to get starting no that is larger
# to get ending no that is lower
# generate no from starting to ending

s = int(input("Enter a starting no, that is larger"))# 10
e = int(input("Enter a ending no that is lower"))   # 1
for i in range(s, e-1, -1):  
    print(i)
    # 10, 9, 8, 7.... 1
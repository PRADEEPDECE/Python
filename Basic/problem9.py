# to make a table of user entered number

num = int(input("Enter a number"))
print("You entered "+str(num))
# 1 * 2 = 2
# 2 * 2 = 4
for i in range(1,11):
    print(str(i)+" * "+str(num)+" = "+str(i*num))

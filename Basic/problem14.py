# to get 6 number 
# store to list
# sum and dispaly resutl to user

lst = []
# to get number from the user and store to list
for i in range(6): # 0 1 2 3 4 5
    lst.append(int(input("Enter 6 number")))

#print("This is the list")
#print(lst)

# To sum number of the list
s = 0
for i in lst:
    s += i
print("Sum of number in the list "+str(s))
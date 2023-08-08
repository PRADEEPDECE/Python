# get six number from the user
# display 
# clear list
# then display

lst = []
# to get number from the user and store to list
for i in range(6): # 0 1 2 3 4 5
    lst.append(int(input("Enter 6 number")))

print("This is the list")
print(lst)
lst.clear()
print("We have removed the list items")
print(lst)
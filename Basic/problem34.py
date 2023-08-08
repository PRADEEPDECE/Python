# get 5 color from the user
# display color
# rm last color
# display

color_lst = []
for i in range(5): # 0 1 2 3 4
    color_lst.append(input("Enter a color name"))
    
print("List color element "+str(color_lst))
color_lst.pop()
print("List color element "+str(color_lst))


# get 5 number from the user
# store in the array and display 
# find max

import array as arr

a = arr.array('i',[])

for i in range(5): 
    a.append(int(input("Enter a number to store in the array")))
m = a[0] # 2,3,4,5,6
for j in range(5):
    print(a[j])
    if(a[j] > m):
        m = a[j]
print("Max Number = "+str(m))

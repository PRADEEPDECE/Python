# to get 5 number from the user
# store in the list
# pass that list to the function 
# inside the function, find * and + 
# dispaly result to the user


lst = []

for i in range(5): # 0 1 2 3 4
    lst.append(int(input("Enter a number to store in the list")))
#print(lst)

def add_mul(lst_num):
    s = 0
    m =  1
    for i in lst_num:
        s += i
        m *= i  
    print("Addition = "+str(s))
    print("Multiplicaiton = "+str(m))
    
add_mul(lst)
    
    
    
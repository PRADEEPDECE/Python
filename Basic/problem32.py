# to get 2 number 
# pass to function 
# max

x = int(input("Enter a numebr"))
y = int(input("Enter b numebr"))

def max_num(a, b):
    print("This result is coming from the function")
    print("a = "+str(a))
    print("b = "+str(b))
    if(a > b):
        print("A is greater")
    else:
        print("B is greater")

max_num(x, y)
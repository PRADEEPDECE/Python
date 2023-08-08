# to get username
# 5 subject marks 
# dispaly total, and every subject marks ind:
import array as arr

user = input("Enter your name ")
a = arr.array('i',[])
print("Enter subject marks in this order English, AI, Physics, Computer, Math")

for i in range(5): #0, 1 , 2, 3, 4
    a.append(int(input("Enter subject mars")))
total = 0
for i in range(5): #0, 1 , 2, 3, 4
    total += a[i] # a[0] => 50, a[1] =>60 


print("Hi, "+user+"!")
print("Your marks is"+str(total))
print("See your all subject marks")
print("English = "+str(a[0]))
print("AI = "+str(a[1]))
print("Physics = "+str(a[2]))
print("Computer = "+str(a[3]))
print("Math = "+str(a[4]))

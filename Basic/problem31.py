# to get students marks
# to find grade
# >=95 A+
# >=80 A
# >=70 B
# >=60 C
# <60 Fail

marks = int(input("Enter your marks to find Grade"))
# '90' -> 90
if(marks >= 95):
    print("Grade is A+")

elif(marks >=80):
    print("Grade is A")

elif(marks >=70):
    print("Grade is B")

elif(marks >=60):
    print("Grade is C") 
else:
    print("Fail")

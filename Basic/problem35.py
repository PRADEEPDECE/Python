# to get 10 student name
# dispaly in desc order

std_name = []

for i in range(10):
    std_name.append(input("Enter name of the Student"))
#print("These are student stored in the list "+str(std_name))

print("Student Name in proper form")
for j in std_name:
    print(j)

std_name.reverse()

print("Student Name in DESC form")
for d in std_name:
    print(d)
# get six marks of the subject
# find total and average 

subj1 = int(input("Enter 1st subject marks"))
subj2 = int(input("Enter 2nd subject marks"))
subj3 = int(input("Enter 3rd subject marks"))
subj4 = int(input("Enter 4th subject marks"))
subj5 = int(input("Enter 5th subject marks"))
subj6 = int(input("Enter 6th subject marks"))

# total
total_result = subj1 + subj2 + subj3 + subj4 + subj5 + subj6

print("Your Total Marks  = "+str(total_result))

# average
ave = total_result/6
print("Your average is = "+str(ave))

# to check user password

pwd = input("Enter your password")

if(pwd.isalnum()):
    print("Your password is okay, that is "+pwd)
else:
    print("Sorry, we did not allow white space and special char in your password that is "+pwd)
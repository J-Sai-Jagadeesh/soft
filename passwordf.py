a=input("Enter the Password:")
l=len(a)
if l<8:
    print("Invalid Password...!\npassword must contain 8 characters")
else:
    upper = False
    lower = False
    digit = False
    special = False
    for char in a:
         if char.isupper():
             upper = True
         elif char.islower():
             lower = True
         elif char.isdigit():
             digit = True
         elif not char.isalnum():
             special = True
    if digit and upper and lower and special:
        print("valid")
    else:
        print("invalid")
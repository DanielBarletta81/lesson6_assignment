#Task 2: Password Complexity Checker
#Create a function that checks the complexity of a user's password. 
#The password must be at least 8 characters long, contain 
#one uppercase letter, one lowercase letter, and one number.
#If the password does not meet these criteria, 
#print a message explaining the complexity requirements.

user_password = input("Enter your Password: ")

def password_checker(user_password):
    
    if len(user_password) >= 8:
        upperCase = False
        lowerCase = False
        number = False

        for char in user_password:
            
            if(char.isupper()):
                upperCase = True
            if(char.islower()):
                lowerCase = True
            if(char.isdigit()):
                number = True

           

        return upperCase and lowerCase and number

    
    else:
        return False

    
                
password_checker(user_password)

if password_checker(user_password) is True:
    print("Password accepted!!")
else:
    print("Invalid password. Password must be at least 8 characters, and must contain one: uppercase letter, lowercase letter, and number")



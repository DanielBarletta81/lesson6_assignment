# Task 3: Email Formatter
#Implement a script that ensures all user email addresses are in a standard format

user_email_addresses = ["apeneck@hotmail.com", "dbarcelona@gmail.com", "pirate@.com", "@gmail.com", "coding@email.com"]

def is_valid_format(user_email_addresses):
    
    for email in user_email_addresses:
         
         local, domain = email.split("@")

         if email.count("@") != 1:
              return False
         if len(local) == 0 or len(domain) == 0:
              return False
         if domain.find('.') == -1:
              return False

    return True

if is_valid_format(user_email_addresses):
     print("All user email addresses are valid.")
else:
     print("Not all emails are in the standard format.")
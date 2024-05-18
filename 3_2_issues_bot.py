#Task 2: Issue Categorizer
# If the user's input contains the word "issue", 
#further categorize the issue based on keywords such as "login", "performance", "error", etc. 
#Print out the category of the issue for the support team.


user_query = input("What is your question? ")

commands = ["help", "issue", "contact support"]

issues = ["login", "error", "crash"]

def help_desk_bot():
    for command in commands:

        identify_word = user_query.find(command)

     
            
        if identify_word != -1 and command == "help":
            print(f"It looks like you need some {command}, How can I help you?")
            
            
            
        if identify_word != -1 and command == "issue":
            print(f"It sounds like you have an {command}, Can you describe the {command} you are having?")
            for issue in issues:
                issue_keyword = user_query.find(issue)
                if issue_keyword != -1 and issue == "login":
                    print(f"The user is having an issue with their {issue}")
                if issue_keyword != -1 and issue == "error":
                    print(f"The user is describing an {issue} they've encountered.")
                if issue_keyword != -1 and issue == "crash":
                    print(f"The user had the program {issue} on them.")
            

        if identify_word != -1 and command == "contact support":
            print(f"You mentioned you want to {command}, I will forward this matter to the support team.")
            
        
            
            

help_desk_bot()
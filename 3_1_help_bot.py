#Task 1: Command Parser
# The aim of this assignment is to create an interactive help desk bot
# that processes user queries and responds appropriately

#Write a script that takes a user's text input and identifies if it contains
#one of the predefined commands (e.g., "help", "issue", "contact support").
#If a command is found, print a response related to the command.

user_query = input("What is your question? ")

commands = ["help", "issue", "contact support"]

def help_desk_bot():
    for command in commands:

        identify_word = user_query.find(command)

     
            
        if identify_word != -1 and command == "help":
            print(f"It looks like you need some {command}, How can I help you?")
            
            
            
        if identify_word != -1 and command == "issue":
            print(f"It sounds like you have an {command}, Can you describe the {command} you are having?")
            

        if identify_word != -1 and command == "contact support":
            print(f"You mentioned you want to {command}, I will forward this matter to the support team.")
            
        
            
            

help_desk_bot()
    
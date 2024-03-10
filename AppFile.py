# Name: Susana Xiao
# Assignment: Quarterly Assessmment 1 
# Class: DS 3850 - 001
# Date: 3/7/24

# Importing the sqlite3 module which establishes a connection to the database.
import sqlite3

# The connection function is then used to call the database name 'questions.db', and then we add one last variable called cursor to execute the connection to the database.
connection = sqlite3.connect ('questions.db')
cursor = connection.cursor()

# Printing statements for the user to pick which category of the Quiz Bowl Game they would like to play.
print ("Welcome to the Quiz Bowl Game: Pick a category from 1-5:")
print ("1. Money and Banking")
print ("2. Business Analytics")
print ("3. Business Database Management")
print ("4. Principles Accounting")
print ("5. Operations, Logistics, and SCM")

# Input statements asking the user to choose from the following 5 categories.
# If and elif statements that changes category to table name based off of user inputs.
user_input = input ("Your category of choice (1-5): ")

if user_input == "1":
    category = "MoneyAndBanking"

elif user_input == "2":
    category = "BusinessAnalytics"

elif user_input == "3":
    category = "BusinessDatabaseManagement"

elif user_input == "4":
    category = "PrinciplesAccounting"

elif user_input == "5":
    category = "OperationsLogisticsSCM"

# The message variable is SQL command that changes table based off of category variable.
msg = "SELECT question, answer FROM " + category

# The execute method allows us to perform some execution on our db object, and retrieving data from the 'question' and 'answer' columns of the 'QuestAns' database table.
# The fetchall is used to retrieve all rows at once and converting it into dictionaries.
cursor.execute (msg)
quiz_Questions = dict (cursor.fetchall())

# Creating a for loop that allows user to input there answers to the questions.
# An "if" and "else" statement providing feedback on if the user's answer match the correct answer from the dictionary.
# Inputting a changing text color function to display the correct and incorrect messages in green and red, respectively. Then the '\033[0m is used to reset the text bakc to white. 
for questions in quiz_Questions:
    print (questions)
    user_answer = input ("Your answer: ")
    if user_answer.lower() == str(quiz_Questions[questions]).lower():
        print ("\033[38;2;0;225;0mCorrect!\033[0m")
    else:
        print ("\033[38;2;225;0;0mIncorrect. The correct answer is: ", quiz_Questions[questions], "\033[0m")

print ("Quiz ended.")

# Closing the cursor and the database connection.
cursor.close()
connection.close()











    


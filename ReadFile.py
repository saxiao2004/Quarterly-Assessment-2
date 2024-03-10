# Name: Susana Xiao
# Assignment: Quarterly Assessmment 1 
# Class: DS 3850 - 001
# Date: 3/9/24

import sqlite3

# Defining the function of 'print_table_data' for it to call a specified parameter 'table_name'.
# Setting the name of the sqlite3 database file as 'questions.db'
# Establishing a connection to the database_file which will is named 'questions.db'.
def print_table_data (table_name):
    database_file = 'questions.db'
    connection = sqlite3.connect (database_file)
    cursor = connection.cursor()

# Executing the connection to the database by making it select the table name 'MoneyAndBanking' and extracting all the question/data from the database.
    cursor.execute (f"SELECT * FROM {table_name};")
    data = cursor.fetchall()

# Printing the string 'table_name' which would be 'MoneyAndBanking' and running through the database to print each row of questions and answers.
    print(f"\nTable: {table_name}")        

    for row in data:
        print(row)

print_table_data('MoneyAndBanking')


# Defining the function of 'print_table_data' for it to call a specified parameter 'table_name'.
# Setting the name of the sqlite3 database file as 'questions.db'
# Establishing a connection to the database_file which will is named 'questions.db'.
def print_table_data (table_name):
    database_file = 'questions.db'
    connection = sqlite3.connect (database_file)
    cursor = connection.cursor()

# Executing the connection to the database by making it select the table name 'BusinessAnalytics' and extracting all the question/data from the database.
    cursor.execute (f"SELECT * FROM {table_name};")
    data = cursor.fetchall()

# Printing the string 'table_name' which would be 'BusinessAnalytics' and running through the database to print each row of questions and answers.
    print(f"\nTable: {table_name}")        

    for row in data:
        print(row)

print_table_data('BusinessAnalytics')


# Defining the function of 'print_table_data' for it to call a specified parameter 'table_name'.
# Setting the name of the sqlite3 database file as 'questions.db'
# Establishing a connection to the database_file which will is named 'questions.db'.
def print_table_data (table_name):
    database_file = 'questions.db'
    connection = sqlite3.connect (database_file)
    cursor = connection.cursor()

# Executing the connection to the database by making it select the table name 'BusinessDatabaseManagement' and extracting all the question/data from the database.
    cursor.execute (f"SELECT * FROM {table_name};")
    data = cursor.fetchall()

# Printing the string 'table_name' which would be 'BusinessDatabaseManagement' and running through the database to print each row of questions and answers.
    print(f"\nTable: {table_name}")        

    for row in data:
        print(row)

print_table_data('BusinessDatabaseManagement')


# Defining the function of 'print_table_data' for it to call a specified parameter 'table_name'.
# Setting the name of the sqlite3 database file as 'questions.db'
# Establishing a connection to the database_file which will is named 'questions.db'.
def print_table_data (table_name):
    database_file = 'questions.db'
    connection = sqlite3.connect (database_file)
    cursor = connection.cursor()

# Executing the connection to the database by making it select the table name 'PrincipleAccounting' and extracting all the question/data from the database.
    cursor.execute (f"SELECT * FROM {table_name};")
    data = cursor.fetchall()

# Printing the string 'table_name' which would be 'PrinciplesAccounting' and running through the database to print each row of questions and answers.
    print(f"\nTable: {table_name}")        

    for row in data:
        print(row)

print_table_data('PrinciplesAccounting')


# Defining the function of 'print_table_data' for it to call a specified parameter 'table_name'.
# Setting the name of the sqlite3 database file as 'questions.db'
# Establishing a connection to the database_file which will is named 'questions.db'.
def print_table_data (table_name):
    database_file = 'questions.db'
    connection = sqlite3.connect (database_file)
    cursor = connection.cursor()

# Executing the connection to the database by making it select the table name 'OperationsLogisticsSCM' and extracting all the question/data from the database.
    cursor.execute (f"SELECT * FROM {table_name};")
    data = cursor.fetchall()

# Printing the string 'table_name' which would be 'OperationsLogisticsSCM' and running through the database to print each row of questions and answers.
    print(f"\nTable: {table_name}")        

    for row in data:
        print(row)

print_table_data('OperationsLogisticsSCM')






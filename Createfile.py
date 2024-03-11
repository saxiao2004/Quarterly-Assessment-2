# Name: Susana Xiao
# Assignment: Quarterly Assessmment 1 
# Class: DS 3850 - 001
# Date: 3/7/24

# Importing the sqlite3 module which establishes a connection to the database.
# Inputting a variable called connection which establishes the database name as 'questions.db'.
# Create a cursor variable to interact with the database.

import sqlite3

connection = sqlite3.connect ('questions.db')
cursor = connection.cursor()

# Cursor method to extract all the records from the tables being created.
# Tables should be created with those attributes/column names.
cursor.execute ("""
CREATE TABLE IF NOT EXISTS MoneyAndBanking (
    id INTEGER PRIMARY KEY,
    question TEXT,
    answer TEXT)
                """)

# Executing SQL query in insert data in the "Money and Banking" table
def add_MoneyBanking (id, question, answer):
    cursor.execute(f"""
        INSERT INTO MoneyAndBanking (id, question, answer)
        VALUES (?,?,?) """,(id, question, answer))

# The function will have attributes of id, questions, and answers for the table of Money and Banking.
add_MoneyBanking (1, "What's the main purpose of a checking account?", "Handling everyday transactions like deposits, withdrawals, and payments.")
add_MoneyBanking (2, "Simple vs. Compound Interest - what's the difference?", "Simple interest applies to the initial amount, while compound interest considers both the principles and accured interest.")
add_MoneyBanking (3, "Why does the FDIC exist?", "To insure bank deposits up to a certain limit, providing finaicial security in case of a bank failure.")
add_MoneyBanking (4, "How does the money multiplier relate to fractional reserve banking?", "Money multiplier shows how functional reserve banking allows banks to create money by lending a portion of deposits.")
add_MoneyBanking (5, "What's the role of Open Market Operations in monetary policy?", "Open market operations involve buying and selling securities to control the money supply and influence interest rates.")
add_MoneyBanking (6, "Define liquidity in banking", "Liquidity is the ease of converting assets into cash, vital for meeting withdrawl demands and financial obligations.")
add_MoneyBanking (7, "What is the primary function of the Reserve Requirement in banking?", "The reserve requirement mandates banks to keep a certain percentage of customer deposits in reserve, controlling the amount of money avaiable for lending.")
add_MoneyBanking (8, "Why is the Federal Funds Rate important?", "It influence overall interest rates and guides monetary policy by representing the overnight lending rate among banks.")
add_MoneyBanking (9, "Define 'moral hazard' in banking", "It is the risk of takingexcessive risks when protected from consequences, often due to government support or insurance.")
add_MoneyBanking (10, "SEC's role in financial markets?", "The SEC regulates securities markets, ensuring investor protection, fair markets, and faciliating capital formation in the U.S.")

# Creating a table with the attributes of Business Analytics
cursor.execute ("""
CREATE TABLE IF NOT EXISTS BusinessAnalytics (
    id INTEGER PRIMARY KEY,
    question TEXT,
    answer TEXT)
                """)

# Executing SQL query in insert data in the "Business Analytics" table
def add_BusinessAnalytics (id, question, answer):
    cursor.execute(f"""
        INSERT INTO BusinessAnalytics (id, question, answer)
        VALUES (?,?,?) """,(id, question, answer))

# The function will have attributes of id, questions, and answers for the table of Business Analytics.
add_BusinessAnalytics (1, "What is the significance of regression analysis in business analytics?", "Regression analysis helps explore relationships between dependent and independent variables, aiding in prediction and understanding correlations.")
add_BusinessAnalytics (2, "Define data mining in the context of business analytics.", "Data mining involves extracting valuable patterns and information from large datasets to support decision-making processes.")
add_BusinessAnalytics (3, "What is the primary goal of time series analysis in business analytics?", "Time series analysis aims to understand and predict trends in data over time, facilitating forecasting and strategic planning.")
add_BusinessAnalytics (4, "Explain the concept of data cleansing in analytics.", "Data cleansing involves identifying and correcting errors or inconsistencies in datasets to ensure accurate and reliable analyses.")
add_BusinessAnalytics (5, "What role does a dashboard play in business analytics?", "Dashboards provide a visual representation of key performance indicators and metrics, allowing for quick and intuitive data analysis.")
add_BusinessAnalytics (6, "How does data visualization contribute to business analytics?", "Data visualization uses charts and graphs to represent complex data, making it easier to understand patterns and trends.")
add_BusinessAnalytics (7, "Define cohort analysis.", "Cohort analysis groups data by shared characteristics to track and compare the performance of specific segments over time.")
add_BusinessAnalytics (8, "Explain the significance of a correlation coefficient in analytics.", "A correlation coefficient measures the strength and direction of a linear relationship between two variables.")
add_BusinessAnalytics (9, "Define predictive analytics.", "Predictive analytics uses statistical algorithms to forecast future trends based on historical data patterns.")
add_BusinessAnalytics (10, "What is descriptive analytics?", "Descriptive analytics involves analyzing historical data to understand past trends and make informed decisions.")

# Creating a table with the attributes of Business Database Management
cursor.execute ("""
CREATE TABLE IF NOT EXISTS BusinessDatabaseManagement (
    id INTEGER PRIMARY KEY,
    question TEXT,
    answer TEXT)        
                """)

# Executing SQL query in insert data in the "Business Database Management" table
def add_BusinessDatabase (id, question, answer):
    cursor.execute(f"""
        INSERT INTO BusinessDatabaseManagement (id, question, answer)
        VALUES (?,?,?) """,(id, question, answer))

# The function will have attributes of id, questions, and answers for the table of Business Database Management.
add_BusinessDatabase (1, "What is a database schema?", "A database schema defines the structure of a database, including tables, relationships, and constraints.")
add_BusinessDatabase (2, "Define data warehousing and its role in business intelligence.", "Data warehousing involves the collection and storage of large volumes of historical data for analysis and reporting in business intelligence systems.")
add_BusinessDatabase (3, "Explain the concept of a foreign key in a database.", "A foreign key establishes a link between tables by referencing the primary key of another table, maintaining referential integrity.")
add_BusinessDatabase (4, "What is the difference between a database and a data warehouse?", "A database stores and manages structured data, while a data warehouse is designed for analytical processing and reporting.")
add_BusinessDatabase (5, "What is the purpose of a primary key in a database table?", "A primary key uniquely identifies each record in a table, ensuring data integrity and providing a reference for relationships.")
add_BusinessDatabase (6, "Why is data normalization important in database design?", "Data normalization reduces redundancy and improves data integrity by organizing information efficiently in a relational database.")
add_BusinessDatabase (7, "Explain the difference between a database view and a table.", "A table stores actual data, while a view is a virtual table generated by a query, representing a subset of data from one or more tables.")
add_BusinessDatabase (8, "What is data replication in the context of database management?", "Data replication involves duplicating data across multiple database servers to improve availability, reliability, and performance.")
add_BusinessDatabase (9, "How does normalization support database design?", "Normalization minimizes data redundancy and dependency issues by organizing data into well-structured tables, improving overall database design.")
add_BusinessDatabase (10, "What is a database index, and why is it used?", "A database index is a data structure that enhances the speed of data retrieval operations on a database table by providing quick access to specific rows.")

# Creating a table with the attributes of Principles of Accounting
cursor.execute ("""
CREATE TABLE IF NOT EXISTS PrinciplesAccounting (
    id INTEGER PRIMARY KEY,
    question TEXT,
    answer TEXT)
                """)

# Executing SQL query in insert data in the "Principles of Accounting" table
def add_Accounting (id, question, answer):
    cursor.execute(f"""
        INSERT INTO PrinciplesAccounting (id, question, answer)
        VALUES (?,?,?) """,(id, question, answer))

# The function will have attributes of id, questions, and answers for the table of Principles of Accounting II.
add_Accounting (1, "What is the purpose of a cash basis accounting method?", "The cash basis recognizes revenues and expenses only when cash is received or paid, providing a straightforward approach for small businesses.")
add_Accounting (2, "What is the significance of the matching principle in accounting?", "The matching principle requires expenses to be recorded in the same period as the revenues they help generate, ensuring accurate financial reporting.")
add_Accounting (3, "What is the difference between a debit and a credit in accounting?", "Debits increase assets and expenses while decreasing liabilities and revenues. Credits have the opposite effect, increasing liabilities and revenues while decreasing assets and expenses.")
add_Accounting (4, "Define the concept of retained earnings.", "Retained earnings represent the cumulative net income of a company that is not distributed as dividends, contributing to shareholder equity.")
add_Accounting (5, "Explain the difference between a journal and a ledger.", "A journal records individual transactions in chronological order, while a ledger organizes and summarizes those transactions by account.")
add_Accounting (6, "What is the difference between a liability and an expense?", "Liabilities are obligations owed to external parties, while expenses are costs incurred in the process of generating revenue.")
add_Accounting (7, "What is the purpose of the double-entry accounting system?", "The double-entry system ensures that every transaction has equal and opposite effects on at least two accounts, maintaining the accounting equation.")
add_Accounting (8, "Define accrual accounting.", "Accrual accounting recognizes revenues and expenses when they are earned or incurred, regardless of when the cash is received or paid.")
add_Accounting (9, "Explain the principle of materiality in accounting.", "Materiality considers the impact of an item on financial statements and whether its omission or misstatement could influence decisions of financial statement users.")
add_Accounting (10, "What is the purpose of the statement of cash flows?", "The statement of cash flows reports the cash inflows and outflows from operating, investing, and financing activities, providing insights into a company's cash position.")

# Creating a table with the attributes of Operations, Logistics, & SCM
cursor.execute ("""
CREATE TABLE IF NOT EXISTS OperationsLogisticsSCM (
    id INTEGER PRIMARY KEY,
    question TEXT,
    answer TEXT)
                """)

# Executing SQL query in insert data in the "Operation, Logistics, & SCM" table
def add_OperationSCM (id, question, answer):
    cursor.execute(f"""
        INSERT INTO OperationsLogisticsSCM (id, question, answer)
        VALUES (?,?,?) """,(id, question, answer))

# The function will have attributes of id, questions, and answers for the table of Principles of Accounting II.
add_OperationSCM (1, "What is the primary goal of supply chain management?", "The primary goal of supply chain management is to efficiently and cost-effectively coordinate the flow of goods, information, and finances from the supplier to the customer.")
add_OperationSCM (2, "What is the purpose of demand forecasting in supply chain management?", "Demand forecasting helps organizations predict customer demand to optimize inventory levels, production schedules, and distribution.")
add_OperationSCM (3, "Explain the concept of reverse logistics.", "Reverse logistics involves the management of product returns, recycling, and the disposal of goods in the supply chain.")
add_OperationSCM (4, "What is the significance of a logistics network design?", "Logistics network design involves optimizing the structure of distribution channels, warehouses, and transportation to enhance efficiency and reduce costs.")
add_OperationSCM (5, "How does the use of blockchain technology impact supply chain transparency?", "Blockchain technology provides a secure and transparent way to record and verify transactions, enhancing traceability and reducing fraud in the supply chain.")
add_OperationSCM (6, "What is the significance of a bill of lading in transportation management?", "A bill of lading is a legal document that outlines the details of a shipment, serving as a receipt and a contract between the shipper and the carrier.")
add_OperationSCM (7, "What is the role of a safety stock in inventory management?", "Safety stock acts as a buffer to protect against unexpected demand fluctuations, ensuring that there are enough products available to meet customer orders.")
add_OperationSCM (8, "Purpose of WMS?", "Warehouse management system improves efficiency in warehouse operations.")
add_OperationSCM (9, "What is VMI?", "Vendor-managed inventory involves suppliers monitoring and replenishing customer inventory.")
add_OperationSCM (10, "How does cross-docking reduce warehouse time?", "Cross-docking reduces storage time by unloading goods directly from inbound to outbound trucks.")

# Closes the connection with the database.
connection.commit()
connection.close()


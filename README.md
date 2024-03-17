# SQLite-Databases-With-Python
# SQLite Databases with Python

This README provides a guide to working with SQLite databases using Python, covering various topics such as connecting to a database, creating tables, inserting records, querying data, and more.

## Table of Contents

- [What Is A Database](#what-is-a-database)
- [Install Python](#install-python)
- [Install Git Bash Terminal](#install-git-bash-terminal)
- [Connect to Database in Python](#connect-to-database-in-python)
- [Create A Table](#create-a-table)
- [Insert One Record Into Table](#insert-one-record-into-table)
- [Insert Many Records Into Table](#insert-many-records-into-table)
- [Query and Fetchall](#query-and-fetchall)
- [Format Your Results](#format-your-results)
- [Primary Key](#primary-key)
- [Use The Where Clause](#use-the-where-clause)
- [Update Records](#update-records)
- [Delete Records](#delete-records)
- [Order Results](#order-results)
- [And/Or](#andor)
- [Limiting Results](#limiting-results)
- [Delete (Drop) A Table And Backups](#delete-drop-a-table-and-backups)
- [Unit 18 Our App - Show All Function](#unit-18-our-app---show-all-function)
- [Unit 19 Our App - Add A Record Function](#unit-19-our-app---add-a-record-function)
- [Unit 20 Our App - Delete a Record Function](#unit-20-our-app---delete-a-record-function)
- [Unit 21 Our App - Add Many Records Function](#unit-21-our-app---add-many-records-function)
- [Unit 22 Our App - Where Clause Function](#unit-22-our-app---where-clause-function)

## What Is A Database

A database is a structured collection of data that allows for efficient storage, retrieval, and manipulation of information. SQLite is a lightweight, serverless, self-contained database engine that is widely used for embedded systems and small to medium-scale applications.

## Install Python

To work with SQLite databases in Python, you need to have Python installed on your system. You can download and install Python from the [official website](https://www.python.org/downloads/).

## Install Git Bash Terminal

Git Bash is a terminal emulator for running the Bash shell on Windows. You can download and install Git Bash from the [official website](https://gitforwindows.org/).

## Connect to Database in Python

To connect to an SQLite database in Python, you can use the `sqlite3` module.

```python
import sqlite3

# Connect to the database
connection = sqlite3.connect('example.db')
```
## Create A Table
You can create a table in an SQLite database using the CREATE TABLE statement.

```
# Create a cursor object
cursor = connection.cursor()

# Execute a SQL statement to create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL
                  )''')

# Commit the transaction
connection.commit()
```
## Insert One Record Into Table
You can insert a single record into a table using the INSERT INTO statement.

```
# Insert a single record into the table
cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('john_doe', 'john@example.com'))

# Commit the transaction
connection.commit()
```
## Insert Many Records Into Table
You can insert multiple records into a table using the executemany() method.

```
# Define a list of records
records = [
    ('jane_doe', 'jane@example.com'),
    ('alice_smith', 'alice@example.com'),
    ('bob_jones', 'bob@example.com')
]

# Insert multiple records into the table
cursor.executemany("INSERT INTO users (username, email) VALUES (?, ?)", records)

# Commit the transaction
connection.commit()
```
## Query and Fetchall
You can query data from a table and fetch all rows using the SELECT statement and the fetchall() method.

```
# Execute a SQL statement to select all records from the table
cursor.execute("SELECT * FROM users")

# Fetch all rows
rows = cursor.fetchall()

# Print the results
for row in rows:
    print(row)
```
## Format Your Results
You can format the query results for better readability.

```
# Format the results
for row in rows:
    print(f"ID: {row[0]}, Username: {row[1]}, Email: {row[2]}")
```
## Primary Key
A primary key is a unique identifier for each record in a table. It ensures that each row is uniquely identifiable.

```
# Create a table with a primary key
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    email TEXT NOT NULL
                  )''')
```
Use The Where Clause
You can use the WHERE clause to filter records based on specific conditions.
```
# Execute a SQL statement with a WHERE clause
cursor.execute("SELECT * FROM users WHERE username=?", ('john_doe',))
```
## Update Records
You can update existing records in a table using the UPDATE statement.

```
# Execute a SQL statement to update a record
cursor.execute("UPDATE users SET email=? WHERE username=?", ('john@example.org', 'john_doe'))
```
## Delete Records
You can delete records from a table using the DELETE FROM statement.

```
# Execute a SQL statement to delete a record
cursor.execute("DELETE FROM users WHERE username=?", ('john_doe',))
```
## Order Results
You can order the query results based on specific columns using the ORDER BY clause.

```
# Execute a SQL statement with an ORDER BY clause
cursor.execute("SELECT * FROM users ORDER BY username")
```
## And/Or
You can use the AND and OR operators to combine multiple conditions in a WHERE clause.

```
# Execute a SQL statement with multiple conditions
cursor.execute("SELECT * FROM users WHERE username=? AND email=?", ('john_doe', 'john@example.com'))
```
## Limiting Results
You can limit the number of rows returned by a query using the LIMIT clause.
```
# Execute a SQL statement with a LIMIT clause
cursor.execute("SELECT * FROM users LIMIT 5")
```
## Delete (Drop) A Table And Backups
You can delete a table and create backups of your database using the DROP TABLE statement and file system operations.

```
# Execute a SQL statement to drop a table
cursor.execute("DROP TABLE IF EXISTS users")


# Create a backup of the database
import shutil
shutil.copyfile('example.db', 'example_backup.db')
```
## Unit 18 Our App - Show All Function
In this unit, we implement a function to display all records from the database.

```
def show_all_records():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

```
## Unit 19 Our App - Add A Record Function
In this unit, we implement a function to add a new record to the database.

```
def add_record(username, email):
    cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email))
    connection.commit()
```

## Unit 20 Our App - Delete a Record Function
In this unit, we implement a function to delete a record from the database.

```
def delete_record(username):
    cursor.execute("DELETE FROM users WHERE username=?", (username,))
    connection.commit()
```

## Unit 21 Our App - Add Many Records Function
In this unit, we implement a function to add multiple records to the database.

```
def add_many_records(records):
    cursor.executemany("INSERT INTO users (username, email) VALUES (?, ?)", records)
    connection.commit()
```
## Unit 22 Our App - Where Clause Function
In this unit, we implement a function to query records based on specific conditions.

```
def search_records(username):
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
```


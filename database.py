import sqlite3

# In-memory database - you can't use if after, disappears when your program ends
# conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('customer.db')

# create a cursor - sort of what tells the db what you want to do
cursor = conn.cursor()

# create a table - doc strings
# cursor.execute("""
#     CREATE TABLE customers(
#                first_name TEXT,
#                last_name TEXT,
#                email_address TEXT
#     );
# """)

# inserting one record into a table

# cursor.execute("INSERT INTO customers VALUES ('Mary', 'Kelly', 'Mary@gmail.com')");

# Inserting many records into a table

many_customers =[('Wes', 'Brown', 'Wes@brown.com'),
                 ('Kim', 'Abram', 'Kim@abram.com'),
                 ('Tiff', 'Kien','tif@ken.com')
                 ]


# cursor.executemany("INSERT INTO customers VALUES (?,?,?)",many_customers)



'''
Data types
    * NULL - doesn't exist
    * INTEGERS - whole number
    * REAL - decimal
    * BLOB - just as it is ex. image
    * TEXT - alphanumeric
'''

# Query the database
cursor.execute("SELECT * FROM customers")

# print(cursor.fetchone()[0]) # print the first thing
# print(cursor.fetchmany(3)) # print 3 elements
# print(cursor.fetchall())

items = cursor.fetchall()
# print(items)

# looping
for item in items:
    print(item[1] + " - " +  item[2])

# commit our connection to database
conn.commit()

# close our connection
conn.close()


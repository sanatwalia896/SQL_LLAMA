import sqlite3

## connect to sqlilte

connection = sqlite3.connect("StudentDb.db")

## create cursor object to insert record,create table

cursor = connection.cursor()
### create table

table_info = """
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT)
"""
cursor.execute(table_info)

## Insert some more records
cursor.execute("""Insert Into STUDENT values('Sanat','generative Ai ','A+',95)""")
cursor.execute("""Insert Into STUDENT values('Rajat','hotel Management' ,'B+',78)""")
cursor.execute("""Insert Into STUDENT values('Taran','Data Science' ,'A',90)""")
cursor.execute("""Insert Into STUDENT values('Ria','Psychology' ,'A+',99)""")
cursor.execute("""Insert Into STUDENT values('Nandini','pharmacy' ,'A',88)""")

# Display all the records

data = cursor.execute("""Select * from STUDENT""")

for row in data:
    print(row)

## commit your changes in the database

connection.commit()
connection.close()

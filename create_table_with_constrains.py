import sqlite3

sqliteConnection = sqlite3.connect("sql.db")
cursor = sqliteConnection.cursor()

#create table
crate_table_query =""" 
CREATE TABLE IF NOT EXISTS STUDENTS 
(id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,  
                    age INTEGER CHECK (age >= 0),  
                    email TEXT UNIQUE,  
                    grade TEXT DEFAULT 'A',  
                    CONSTRAINT grade_check CHECK (grade IN ('A', 'B', 'C', 'D', 'F'))  
)
"""
# cursor.execute(crate_table_query)
# print("Table created successfully")
#insert data
# insert_query = """
# INSERT INTO STUDENTS (id, name, age ,email, grade) 
# VALUES (9,"varsha","25","varsha@gmail.com","C")  """
# cursor.execute(insert_query)
# print("Table inserted successfully")
#update 
update_query = """
UPDATE  STUDENTS
SET  name ='joy',age='20', email='joy@gmail.com',grade='C' 
 WHERE id = 1
 """
cursor.execute(update_query)
sqliteConnection.commit()

#delete
# delete_query = "DELETE FROM STUDENTS WHERE id = 1"  #delete query
# cursor.execute(delete_query)
select_query=("SELECT * FROM STUDENTS")
# select_query=("SELECT name,email FROM STUDENTS")
# select_query=("SELECT * FROM STUDENTS order by age desc") #displays datas in desc order
# select_query=("SELECT distinct age FROM STUDENTS ") #distinct or unique value
# select_query=("SELECT * FROM STUDENTS where name= 'ram' and age= '25'") #using and operation
# select_query=("SELECT * FROM STUDENTS where name= 'ram' or age= '20'") #using or operation
# select_query=("SELECT * FROM STUDENTS limit 1")#limit the column 
# select_query=("SELECT * FROM STUDENTS where age in (23,25)") # in operation
# select_query=("SELECT * FROM STUDENTS where age not in (23,25)")#not in operation
# select_query=("SELECT max (age) FROM STUDENTS")#aggregate functions
# select_query=("SELECT max (name) FROM STUDENTS")#aggregate functions
# select_query=("SELECT avg(age) FROM STUDENTS")#aggregate functions
# select_query=("SELECT count (age) FROM STUDENTS")#aggregate functions
# select_query=("SELECT sum(age) FROM STUDENTS")#aggregate functions
# select_query=("SELECT name,age,sum(age) FROM STUDENTS group by 1,2")#aggregate functions by particular column use group by
# select_query=("SELECT name,max(age) FROM STUDENTS group by 1")#aggregate functions
cursor.execute(select_query)
rows = cursor.fetchall()
 # Print the rows
for row in rows:
    print(row)
# print("Data deleted successfully.") 
cursor.close()
sqliteConnection.close()


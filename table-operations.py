import sqlite3

sqliteConnection = sqlite3.connect("sql.db")
cursor = sqliteConnection.cursor()

#create table
create_table ="""
CREATE TABLE IF NOT EXISTS EMP
(id INT PRIMARY KEY,
name TEXT NOT NULL,
age INT CHECK (age >=18),
date_of_joining DATE)
"""
#insert data
insert_data="""
INSERT INTO EMP (id,name,age,date_of_joining ) values(1006,"sari","23","2024-01-5")
"""
#updadte
update ="""
UPDATE EMP SET name="siva",age="20",date_of_joining="2024-01-9" WHERE id=1004
"""

cursor.execute(update)
print("data updated successfully")

select_query=("SELECT * FROM EMP")
#We cant use aggregate fun with where to over come this we are using having
select_query=("SELECT name, COUNT(age) FROM EMP GROUP BY 1 HAVING COUNT(age)")
#If u want give range of value to extract (inclusive)
select_query=("SELECT * FROM EMP WHERE age BETWEEN 22 AND 24")
#alias
select_query=("select date_of_joining as doj from emp")
#wildcards(stars with word a and ends with rest of  the pattern)
select_query=("select * from emp where name like'%i'")
# _will work with one word- at a time ,_no of underscores take one value at a time
select_query=("select * from emp where name like 'sr_' ") 
#llike -we can extract the capitial or small letters but like wont support 
# select_query=("select * from emp where name llike 'emp'")
#no.of column shld be same
create_table2= """
create table if not exists emp3 (id int, name varchar(50),age int,date_of_joining date)
"""
insert="""
insert into emp3 (id,name,age,date_of_joining ) values(1002,"jeeva","22","2024-03-21")
"""
#union combine emp2 and emp3 table
select_query=("select id,name from emp union select id,name from emp3")
#union all removes duplicate 
select_query=("select id,name from emp union all select id,name from emp3")
#intersection
elect_query=("select id,name from emp intersection select id,name from emp3")

cursor.execute(select_query)

rows = cursor.fetchall()
 # Print the rows
for row in rows:
    print(row)
sqliteConnection.commit()
cursor.close()
sqliteConnection.close()

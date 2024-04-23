import sqlite3

sqliteConnection = sqlite3.connect("sql.db")
cursor = sqliteConnection.cursor()

# Create the 'detail' table with three columns

create_table = """
CREATE TABLE IF NOT EXISTS detail (
    id INT,
        name VARCHAR(50),
            date_of_joining DATE
            )
            """
# cursor.execute(create_table)
# print("Table created successfully")

#Insert a row into the 'detail' table
        insert_query = """
        INSERT INTO detail (id, name, date_of_joining) 
        VALUES (5, 'siva', '2024-04-21')
        """
        cursor.execute(insert_query)
        sqliteConnection.commit()  # Commit the transaction
        
        select_query = "SELECT * FROM detail"
        
        cursor.execute(select_query)
        rows = cursor.fetchall()
         # Print the rows
        for row in rows:
            print(row)
        print("Data inserted successfully.")

#Update rows in the 'details' table
            update_query = """
            UPDATE detail 
            SET name = 'kumar', date_of_joining = '2024-05-01' 
            WHERE id = 1
            """
            cursor.execute(update_query)
            sqliteConnection.commit()  # Commit the transaction
            # select_query = "SELECT * FROM detail"

            # cursor.execute(select_query)
            # rows = cursor.fetchall()
            #  # Print the rows
            # for row in rows:
            #     print(row)
            # print("Data updated successfully.")
# delete query and view the table
            delete_query = "DELETE FROM detail WHERE id = 1"
            cursor.execute(delete_query)
            sqliteConnection.commit()  # Commit the transaction
            select_query = "SELECT * FROM detail"

            cursor.execute(select_query)
            rows = cursor.fetchall()
             # Print the rows
             for row in rows:
                     print(row)
            print("Data deleted successfully.")
# Close the cursor and the connection
cursor.close()
sqliteConnection.close()
     

                     

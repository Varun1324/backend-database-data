import mysql.connector
from mysql.connector import Error
def main():
    try:
        connection = mysql.connector.connect(
            host='sql12.freesqldatabase.com',       
            user='sql12712369',    
            password='eYlZuGDIWK',
            database='sql12712369',
            port='3306'
        )
    except Error as e:
        print(f"Error: {e}")
    print("1. is connected")
    print("2. show users")
    print("3. Insert users")
    option=int(input("select a option"))
    if(option==1):
        connect_to_database(connection)
    elif(option==2):
        show_users(connection)
    elif(option==3):
        insert_user(connection)

def connect_to_database(connection):
    if connection.is_connected():
        print("Successfully connected to the database")
    else:
        print("Unable to connect database")

def show_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT *FROM users;")
    rows=cursor.fetchall()
    for i in rows:
        print(i)
    connection.commit()
    
def insert_user(connection):
    username=input("Enter a username :")
    password=input("Enter a password : ")
    email=input("Enter a email : ")
    cursor = connection.cursor()
    query = 'INSERT INTO users (username, password, email) VALUES (%s, %s, %s)'
    cursor.execute(query, (username, password, email))
    connection.commit()
    print("User inserted successfully")

if __name__ == "__main__":
    main()

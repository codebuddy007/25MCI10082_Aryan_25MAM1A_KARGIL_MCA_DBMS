import mysql.connector
from db import get_db_connection

def register_user(user_id,name, email, password):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="salhgs@cmr23",
        database="crimedb"
    )
    cursor = db.cursor()

    try:
        cursor.execute("INSERT INTO users (user_id,name, email, password) VALUES (%s, %s, %s)", (name, email, password))
        db.commit()
    except mysql.connector.Error as err:
        print("Error: ", err)
    finally:
        cursor.close()
        db.close()

def login_user(email, password):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
        user = cursor.fetchone()
        if user:
            print("Logged in successfully!")
            return user
        else:
            print("Invalid credentials")
            return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()
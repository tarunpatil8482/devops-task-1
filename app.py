import psycopg2 
import time 
# Wait a bit for Postgres to be ready 
time.sleep(5) 
try: 
 conn = psycopg2.connect( 
host="my-postgres", 
database="mydb", 
user="user", 
password="pass" 
) 
 print("Connected to the database!") 
 conn.close() 
except Exception as e: 
 print("Connection failed:", e)
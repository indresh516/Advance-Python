import psycopg2
conn = psycopg2.connect(dbname="postgres", user="postgres", password="Isit@1990",host="localhost",port="5432")

cursor = conn.cursor()
cursor.execute('''create table employees(Name text, ID int, Age int);''')
print("Table Created Successfully")

conn.commit()
conn.close()


import psycopg2
def table():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Isit@1990",host="localhost",port="5433")

    cursor = conn.cursor()
    cursor.execute('''create table employees(Name text, ID int, Age int);''')
    print("Table Created Successfully")

    conn.commit()
    conn.close()

    print("Connected Successfully")

def data():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Isit@1990",host="localhost",port="5432")

    cursor = conn.cursor()
    cursor.execute('''insert into employees(Name, ID, Age) values('Rahul', 01, 22);''')
    print("Data Added Successfully")

    conn.commit()
    conn.close()

data()

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

    name = input('Enter Name : ')
    id = input('Enter Employee ID : ')
    age = input('Enter Employee Age : ')

    query = '''insert into employees(Name, ID, Age) values(%s, %s, %s);'''

    cursor.execute(query,(name,id,age))
    print("Data Added Successfully")

    conn.commit()
    conn.close()

data()

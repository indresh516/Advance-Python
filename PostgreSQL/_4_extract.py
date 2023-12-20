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
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Isit@1990",host="localhost",port="5433")

    cursor = conn.cursor()
    cursor.execute('''insert into employees(Name, ID, Age) values('Rahul', 01, 22);''')
    print("Data Added Successfully")

    conn.commit()
    conn.close()

def extract():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Isit@1990",host="localhost",port="5432")

    cursor = conn.cursor()
    cursor.execute('''select * from employees;''')
    show = cursor.fetchone()
    #fetchone direct use
    # print(cursor.fetchone())
    print("Name          :          ",show[0])
    print("ID            :          ",show[1])
    print("Age           :          ",show[2])
    

    conn.commit()
    conn.close()


extract()

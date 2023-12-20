import psycopg2
connect = psycopg2.connect(dbname="postgres", user="postgres", password="Isit@1990",host="localhost",port="5432")
print("Connected Successfully")
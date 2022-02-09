from pymysql import *

db=connect(host="localhost",user="root",password="")

qry="create database aa"


cur=db.cursor()

cur.execute(qry)

db.close()

print("db created")



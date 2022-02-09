from msilib import Table
from msilib.schema import tables
from venv import create
from pymysql import *

db=connect(host="localhost",user="root",passwd="",database="aa")

#qry="create table student(name varchar(250) not null, rollno varchar(250) not null, place text not null, course text not null, percentage float not null)"

qry="alter table student add primary key(rollno)"

cur=db.cursor()

cur.execute(qry)

#print("table created")

print("Altered")
db.close()
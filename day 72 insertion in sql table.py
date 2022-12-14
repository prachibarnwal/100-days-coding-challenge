import mysql.connector as sql

con = sql.connect(host = 'localhost',user = 'root',password = '',database = 'nov20')

if con.is_connected():
    rno = int(input("Enter Roll Number : "))
    name = input("Enter Name : ")
    age = int(input("Enter Age : "))
    q = "insert into student values(%s,%s,%s)"
    data = (rno,name,age)
    cur1 = con.cursor()
    cur1.execute(q,data)
    con.commit()
    print("STUDENT INSERTED SUCCESSFULLY")
    

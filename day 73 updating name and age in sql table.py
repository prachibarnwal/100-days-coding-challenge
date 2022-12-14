import mysql.connector as sql

con = sql.connect(host = 'localhost',user = 'root',password = '',database = 'nov20')

if con.is_connected():
    rno = int(input("Enter Roll Number to be Updated : "))
    name = input("Enter New Name : ")
    age = int(input("Enter New Age : "))
    q = "update student set sname = %s , age = %s where sid = %s"
    data = (name,age,rno)
    cur1 = con.cursor()
    cur1.execute(q,data)
    con.commit()
    print("STUDENT UPDATED SUCCESSFULLY")
    

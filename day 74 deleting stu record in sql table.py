import mysql.connector as sql

con = sql.connect(host = 'localhost',user = 'root',password = '',database = 'nov20')

if con.is_connected():
    rno = input("Enter Roll Number to be Deleted : ")
    q = "select * from student where sid = "+rno
    cur1 = con.cursor()
    cur1.execute(q)
    ress = cur1.fetchone()
    print(ress)
    ch = input("Do You Want to Delete This Record : (yes/no) ")
    if ch.lower() == "yes":
        q = "delete from student where sid = "+ rno
        cur1.execute(q)
        con.commit()
        print("STUDENT DELETED SUCCESSFULLY")
    else:
        print("OK :')")

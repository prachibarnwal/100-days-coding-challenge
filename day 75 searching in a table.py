import mysql.connector as mycon
con = mycon.connect(host = 'localhost', user = 'root', password = '', database = 'nov20')
if con.is_connected():
    admno = input("Enter Student's Id of The Student : ")
    q = 'select * from student where sid = ' + admno
    cr = con.cursor()
    cr.execute(q)
    res = cr.fetchone()
    if res != None:
        print(res)
    else:
        print("NO STUDENT FOUND")
        

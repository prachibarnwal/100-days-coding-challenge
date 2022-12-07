import mysql.connector as sql

con = sql.connect(host = 'localhost',user = 'root',password = '',database = 'nov20')

if con.is_connected():
    q = "select * from student"
    cur = con.cursor()
    cur.execute(q)
    res = cur.fetchall()
    print("ID\tNAME\tAGE\n")
    for row in res:
        print(row[0],'\t',row[1],'\t',row[2])

    if cur.rowcount == 0:
        print("TABLE IS EMPTY")
    else:
        print(cur.rowcount," Students Processed")
else:
    print("ERROR AAYA")

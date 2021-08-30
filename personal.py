import mysql.connector
from flask import session
import datetime as d
mydb = mysql.connector.connect(
  host='localhost',
  user='root',
  passwd='root',
  database='pythonlogin',
  port='3306',
)

c = mydb.cursor()

def timetable (m):
        c.execute("SELECT image FROM timetable WHERE class=%s",(m,))
        result = c.fetchone()
        return "<a href="+result[0]+">click link to see time table</a>"
def assign():
    try:
        session['user']
    except KeyError:
        return "please enter your roll number to  get personal details and try again"
    ans="<ul>"
    print(session['user'])
    t=int(d.datetime.now().month)
    c.execute("select year from mytable where Roll_no=%s",[session['user']])
    result = c.fetchone()
    y=result[0]
    if(t>=7 and t<=11):
        if(y==1):
            c.execute("select * from sem11")
            re=c.fetchall()
            for x in re:
               ans=ans+"<li>"+x[0]+"      "+"<a href="+x[1]+">click link to see assignment</a></li>"
        if(y==2):
            c.execute("select * from sem21")
            re = c.fetchall()
            for x in re:
                ans = ans + "<li>" + x[0] + "      " + "<a href=" + x[1] + ">click link to see assignment</a></li>"
        if y==3:
            c.execute("select * from sem31")
            re = c.fetchall()
            for x in re:
                ans = ans + "<li>" + x[0] + "      " + "<a href=" + x[1] + ">click link to see assignment</a></li>"
        if y==4:
            c.execute("select * from sem41")
            re = c.fetchall()
            for x in re:
                ans = ans + "<li>" + x[0] + "      " + "<a href=" + x[1] + ">click link to see assignment</a></li>"
    else:
        if (y == 1):
            c.execute("select * from sem12")
            re = c.fetchall()
            for x in re:
                ans = ans + "<li>" + x[0] + "      " + "<a href=" + x[1] + ">click link to see assignment</a></li>"
        if (y == 2):
            c.execute("select * from sem22")
            re = c.fetchall()
            for x in re:
                ans = ans + "<li>" + x[0] + "      " + "<a href=" + x[1] + ">click link to see assignment</a></li>"
        if y == 3:
            c.execute("select * from sem32")
            re = c.fetchall()
            for x in re:
                ans = ans + "<li>" + x[0] + "      " + "<a href=" + x[1] + ">click link to see assignment</a></li>"
        if y == 4:
            c.execute("select * from sem42")
            re = c.fetchall()
            for x in re:
                ans = ans + "<li>" + x[0] + "      " + "<a href=" + x[1] + ">click link to see assignment</a></li>"
    ans=ans+"</ul>"
    return ans

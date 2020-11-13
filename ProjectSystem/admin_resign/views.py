from django.shortcuts import render

from admin_resign.form import resign_form
import MySQLdb
import time
import gettext
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    print request.method
    message = ''
    if request.method == 'POST':
        print 'getPost'
        username = request.POST['stuname']
        userpasswd = request.POST['stupasswd']
        
        
        getData = [request.POST['stuname'],
                   request.POST['stupasswd'],
                   '1',
                   ]
        print username
        print userpasswd

        conn = MySQLdb.connect(host = 'localhost',
                               user = 'root',
                               passwd = '07n0604',
                               port = 3306,
                               db = 'projectsystem',
                               charset = 'utf8')
        cursor = conn.cursor()
        cursor.execute('SET NAMES UTF8')
        cursor.execute('SET CHARACTER SET utf8')
        cursor.execute('SET character_set_connection=utf8')
        cursor.close()
        if conn:
            print 'conn succ'
        try:
            cursor = conn.cursor()
            sql = 'select * from user'
            print sql
            cursor.execute(sql)
            rs = cursor.fetchall()
        except:
            print Exception
        print len(rs)
        cursor.close()
        userid = str(len(rs) + 1)
        getData.insert(0,userid)
        print userid
        
        print getData
    
        try:
            print 'in try'
            sql = "insert into user values('" + getData[0] + "'"
            for item in getData[1:]:
                sql = sql + ",'" + item + "'"
            sql = sql + ')'
            #print getData[0:2]
            #sql = "insert into readers values(%s, %s)" %getData[0:2] 
            #sql = 'insert into readers values('
            print sql

            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            message = "resign success"
        except TypeError, msg:
            conn.rollback()
            message = str(msg)
            print msg
        finally:
            cursor.close()
            conn.close()
            
    return render(request,'admin_resign/resign.html',{"string": message})

from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect

import MySQLdb
from login import forms

# Create your views here.
def index(request):
    if 'username' in request.POST or 'userpassword' in request.POST or 'username' in request.GET and 'userpassword' in request.GET:
        print 'do check'
        return check(request)
    
    username = request.COOKIES.get('username','')
    if username: 
        print 'username:' + username
        position = checkPostion(username)
        return render(request,"login/login.html",{"username":username,"position":position})
    else:
        return render(request,"login/login.html")

def check(request):
    if request.method == "POST":
        print 'getPost'
        if 'username' in request.POST and 'userpassword' in request.POST:
            username = request.POST['username']
            userpassword = request.POST['userpassword']
#        form = forms.LoginForm(request)
#        username = form.username
#        userpassword = form.userpassword
#        print 'get name:' + username
#        print 'get passwd:' + userpassword
    if request.method == "GET":
        print 'Method GET'
        if 'username' in request.GET and 'userpassword' in request.GET:
            username = request.GET['username']
            userpassword = request.GET['userpassword']
            
            
    if not username or not userpassword:
        print 'username:' + username
        print 'userpasswd:' + userpassword
        print "please input username or password"
        return render(request,'login/login.html',{'string':'please input username or password'})
    
    print 'username:' + username
    print 'userpasswd:' + userpassword
    
    conn = MySQLdb.Connect(host = 'localhost',
                           user = 'root',
                           passwd = '07n0604',
                           port = 3306,
                           db = 'projectsystem')
    cursor = conn.cursor()
    sql = "SELECT * FROM user"
    cursor.execute(sql)
    print sql
    rs = cursor.fetchall()
    print rs
    user_success = False
    for raw in rs:
        print raw
        if raw[1] == username:
            if raw[2] == userpassword:
                user_success = True
                if raw[3] == '0':
                    #return render(request, "admin_bookinfo\\book_info.html")
                    response = HttpResponseRedirect('/teacher/project/list/')
                    response.set_cookie('username', username, 3600)
                    return response
                if raw[3] == '1':
                    response = HttpResponseRedirect('/student/project/list/')
                    response.set_cookie('username', username, 3600)
                    return response
    print user_success
    if not user_success:
        return render(request, "login/login.html", {'string':"name or password error"})
    
def logout(request):
    response = HttpResponseRedirect('/login/')
    response.delete_cookie('username')
    return response

def about(request): 
    username = request.COOKIES.get('username','')
    if username: 
        print 'username:' + username
        position = checkPostion(username)
        return render(request,"login/about.html",{"username":username,"position":position})
    else:
        return render(request,"login/about.html")

def checkPostion(username):
    sql = "select Position from user where Name = '" + username + "'"
    conn = MySQLdb.connect(host = 'localhost',
                           user = 'root',
                           passwd = '07n0604',
                           port = 3306,
                           db = 'projectsystem')
    cursor = conn.cursor()
    cursor.execute('SET NAMES UTF8')
    
    cursor.execute(sql)
    rs = cursor.fetchall()
    print 'sql = ' + sql
    print rs

    cursor.close()
    conn.close()
    
    return rs[0][0]

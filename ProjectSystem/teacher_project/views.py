#*- coding: utf-8 -*-

from django.shortcuts import render
import MySQLdb
from django.http.response import HttpResponse


# Create your views here.
def get_data(sql):
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
    return rs

def insert_date(sql):
    conn = MySQLdb.connect(host = 'localhost',
                           user = 'root',
                           passwd = '07n0604',
                           port = 3306,
                           db = 'projectsystem')
    cursor = conn.cursor()
    cursor.execute('SET NAMES UTF8')
    try:
        cursor.execute(sql)
        conn.commit() 
        returnstr = '作业添加成功'   
    except TypeError,msg:
        conn.rollback()
        print msg
    finally:
        cursor.close()
        conn.close()
    return returnstr

def index(request):
    username = request.COOKIES.get('username','')
    print 'username:' + username

    if 'creat_project_name' in request.POST or 'creat_project_name' in request.GET:
        print 'do insert'
        creat_project(request,username)


    sql = 'select Id,name,Author from project' 
    rs = get_data(sql)
    errorString = ''
    if not rs:
        print "no rs"
        errorString = '尚无项目'
    
    tablename = ["Id","name","Author"]
    username = request.COOKIES.get('username','')
    print 'username:' + username
    return render(request,'teacher_projectinfo/project_info.html', {'username':username, "p_info":rs,'tablename':tablename,'string':errorString})

def showproject(request,num):
    sql = "select Id,name,Content,Author from project where Id = '" + num + "'" 
    print sql
    projectResult = get_data(sql)
    errorString = ''
    if not projectResult:
        print "no projectResult"
        errorString = '尚无项目'
        return render(request,'teacher_projectinfo/project_content.html', {'string':errorString})
    

    username = request.COOKIES.get('username','')
    print 'username:' + username

    sql = "select student from projectresult where project = '" + str(projectResult[0][0]) + "'"
    print sql
    project_applyResult = get_data(sql)
    print project_applyResult

    return render(request,'teacher_projectinfo/project_content.html', {'username':username,"applyInfo":project_applyResult, "p_info":projectResult,'string':errorString})
    
def creat_project(request,AuthorName):
    print "do apply"
    creat_project_name = ''
    creat_project_content = ''
    if request.method == "POST":
        print 'getPost'
        creat_project_name = request.POST['creat_project_name']
        creat_project_content = request.POST['creat_project_content']
    else:    
        if request.method == "GET":
            print 'Method GET'
            creat_project_name = request.GET['creat_project_name']
            creat_project_content = request.GET['creat_project_content']
    print creat_project_name
        
    totalNumber = 0
    sql = "select * from project"
    applyedResult = get_data(sql)
    totalNumber = len(applyedResult)
    sql = "insert into project() values('" + str(totalNumber+1) + "','" + str(creat_project_name) + "','" + str(creat_project_content) + "','" + str(AuthorName) + "')"
    print sql
    errorStr = insert_date(sql)
    print errorStr
    return errorStr

def show_project_apply(request,project_number,studentName):
    sql = "select Id,name,Content,Author from project where Id = '" + project_number + "'" 
    print sql
    projectResult = get_data(sql)
    errorString = ''
    if not projectResult:
        print "no projectResult"
        errorString = '尚无项目'
        
    username = request.COOKIES.get('username','')
    print 'username:' + username

    sql = "select id,project,student,content from projectresult where project = '" + str(project_number) + "' and student = '" + studentName + "'"
    print sql
    project_applyResult = get_data(sql)
    project_applyContent = ''
    if project_applyResult :
        project_applyContent = project_applyResult[0][3]
    print project_applyContent

    return render(request,'teacher_projectinfo/project_detail.html', {'username':username,"content":project_applyContent,"studentname":studentName, "p_info":projectResult,'string':errorString})

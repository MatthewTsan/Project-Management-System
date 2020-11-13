#-*- coding: utf-8 -*-

from django.shortcuts import render
import MySQLdb
from django.http.response import HttpResponse

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
    sql = 'select Id,name,Author from project' 
    rs = get_data(sql)
    errorString = ''
    if not rs:
        print "no rs"
        errorString = '尚无项目'
    
    tablename = ["Id","name","Author"]
    username = request.COOKIES.get('username','')
    print 'username:' + username
    return render(request,'student_projectinfo/project_info.html', {'username':username, "p_info":rs,'tablename':tablename,'string':errorString})

def showproject(request,num):
    sql = "select Id,name,Content,Author from project where Id = '" + num + "'" 
    print sql
    projectResult = get_data(sql)
    errorString = ''
    if not projectResult:
        print "no projectResult"
        errorString = '尚无项目'
        
    username = request.COOKIES.get('username','')
    print 'username:' + username



    if 'project_apply' in request.POST or 'project_apply' in request.GET:
        print 'do insert'
        apply_project(request,num,username)



    sql = "select id,project,student,content from projectresult where project = '" + str(projectResult[0][0]) + "' and student = '" + username + "'"
    print sql
    project_applyResult = get_data(sql)
    project_applyContent = ''
    if project_applyResult :
        project_applyContent = project_applyResult[0][3]
    print project_applyContent

    return render(request,'student_projectinfo/project_content.html', {'username':username,"content":project_applyContent, "p_info":projectResult,'string':errorString})
    
def apply_project(request,projectNumber, StudentName):
    print "do apply"
    project_apply = ''
    if request.method == "POST":
        print 'getPost'
        project_apply = request.POST['project_apply']
    else:    
        if request.method == "GET":
            print 'Method GET'
            project_apply = request.GET['project_apply']
    print project_apply
    
    sql = "select * from projectresult where project = '" + projectNumber + "' and student = '" + StudentName + "'"
    print sql
    applyedResult = get_data(sql)
    print applyedResult
    if len(applyedResult) <> 0:
        sql = "update projectresult SET content = '" + str(project_apply) + "' where project = '" + projectNumber + "' and student = '" + StudentName + "'"
    else:
        totalNumber = 0
        sql = "select * from projectresult"
        applyedResult = get_data(sql)
        totalNumber = len(applyedResult)
        sql = "insert into projectresult() values('" + str(totalNumber+1) + "','" + str(projectNumber) + "','" + str(StudentName) + "','" + str(project_apply) + "')"
    print sql
    errorStr = insert_date(sql)
    print errorStr
    print 'laksdjflk '
    return errorStr

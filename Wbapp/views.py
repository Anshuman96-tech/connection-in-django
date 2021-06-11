from django.shortcuts import render

# Create your views here.

#import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="",
#     database="db1",
#     port="3308"
# )
#
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO login1 (User, Password) VALUES (%s, %s)"
# val = [
#     ('Anshuman', '1308'),
#     ('Anish', '1108'),
#
# ]
#
# mycursor.executemany(sql, val)
#
# mydb.commit()
#
# print(mycursor.rowcount, "was inserted.")
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#from pymysql import *
import mysql.connector
con = mysql.connector.connect(
     host="localhost",
    user="root",
     passwd="",
   database="db1",
     port="3308"
 )
#con=Connect(host='127.0',user='root',password='',
cr=con.cursor()
def home(request):
   return render(request, 'signup.html')

@csrf_exempt
def sign(request):
    name = request.POST.get('uname')
    password = request.POST.get('password')
    s= "select * from login1"
    cr.execute(s)
    l=cr.fetchall()
    for i in l:
       if i[0]== name:
          return HttpResponse("Username already existed")
    s="insert into login1 values('{}','{}')".format(name,password)
    #s = "INSERT INTO login1 (username, password) VALUES (name, password)"
    cr.execute(s)
    con.commit()
    return HttpResponse("Data inserted sucesfully")
def login(request):
   return render(request,'login.html')
@csrf_exempt
def logi(request):
    name=request.POST.get('uname')
    password=request.POST.get('password')
    s="select * from login1"
    cr.execute(s)
    l=cr.fetchall()
    for i in l:
        if i[0]==name and i[1]==password:
            return HttpResponse("Login Successful")
    else:
        return HttpResponse('Invalid Login Credentials')

def forget(request):
   return render(request,'forget.html')
@csrf_exempt

def Forgot(request):
   name = request.POST.get('uname')
   s = "select * from login1"
   cr.execute(s)
   l=cr.fetchall()
   for i in l:
      if i[0]==name:
         return HttpResponse(i[1])
   else:
         return HttpResponse('Invalid username')

def change(request):
   return render(request,'change.html')
@csrf_exempt
def chng(request):
   name = request.POST.get('uname')
   password = request.POST.get('password')
   cpass = request.POST.get('cpassword')
   s = "select * from login1"
   cr.execute(s)
   l=cr.fetchall()
   for i in l:
      if i[0]==name and i[1]==password:
         s1 = "update login1 set password='{}' where username='{}'".format(cpass,name)
         cr.execute(s1)
         con.commit()
         return HttpResponse('Successfully changed')
   else:
         return HttpResponse('Invalid username')
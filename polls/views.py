from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import sqlite3


def index(request):
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    cursor.execute('select * from contacts')
    users = ''
    for i in cursor:
        users += str(i)
    return HttpResponse(users)


def print1(request):
    return HttpResponse('Hello world as print (teacher) in polls/views.py changed in polls/urls.py')


def print2(request):
    return HttpResponse('<h3>print2 polls/views.py changed in polls/urls.py</h3>')


def examplePrint(request):
    return HttpResponse("<h3>Privet MIR as examplePrint in polls/views.py</h3>")

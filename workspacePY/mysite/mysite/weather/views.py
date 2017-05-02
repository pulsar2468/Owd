from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.context_processors import request
import sys
import sqlite3
import json
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
from django import forms #i refer to my forms.py
from .forms import MyRegistrationForm #i get My form, because i change the user model authentication
from .forms import SignUpWeatherForm
import sqlite3


def index(request):
    name_city=[]
    conn = sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
    c = conn.cursor()
    sql='SELECT City.name FROM City'
    for row in c.execute(sql):
        name_city.append(row[0])
    conn.close()
    context = {'name_city': name_city}
    return render(request, 'weather/home.html',context) #he renders the template and the data with request http


def real_time(request):
    if request.user.is_authenticated():
        sys.path.insert(0, "/home/nataraja/Scrivania/OpenData")
        import onOpenStreetMap
        onOpenStreetMap.real_time()
        HtmlFile = open('/home/nataraja/Scrivania/OpenData/workspacePY/real_timeMap.html', 'r', encoding='utf-8')
        source_code = HtmlFile.read() 
        return HttpResponse(source_code)
    else:
            return HttpResponse("Before, you have to log in!")


def history(request):
    response=request.GET.get('name', '') #parameters name=city, otherwise null
    latest_list= [] 
    conn = sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
    c = conn.cursor()
    sql = 'SELECT City.id,"%s".name,"%s".detection_time,'\
    'City.lat,City.lon,"%s".temp,"%s".humidity,"%s".wind_speed '\
    'FROM "%s",City WHERE City.name="%s".name'%(response,response,response,response,response,response,response)
    for row in c.execute(sql):
        latest_list.append(row)
    conn.close()
    context = {'list': latest_list}
    htmlResponse=json.dumps({'list':latest_list})
    return HttpResponse(htmlResponse)
    #return render(request,'weather/data_history.html',context)


def all_plot(request):
    if request.user.is_authenticated():
        sys.path.insert(0, "/home/nataraja/Scrivania/OpenData")
        import onOpenStreetMap
        response=request.GET.get('name', '') #parameters name=city, otherwise null
        '''
        latest_list= [] 
        conn = sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
        c = conn.cursor()
        sql = 'SELECT City.id,"%s".name,"%s".detection_time,'\
        'City.lat,City.lon,"%s".temp,"%s".humidity,"%s".wind_speed '\
        'FROM "%s",City WHERE City.name="%s".name'%(response,response,response,response,response,response,response)
        for row in c.execute(sql):
            latest_list.append(row)
        conn.close()
        context = {'list': latest_list}
        '''
        htmlResponse=onOpenStreetMap.schema(response)
        return HttpResponse(htmlResponse)
    else:
        return HttpResponse("Before, You have to log in!")
   
   
#simple APi list   
def api1_0(request):    
    return render(request, 'weather/api1_0.html')
    
    
def city_list(request): 
    #response=request.GET.get('name', '') #parameters name=city, otherwise null
    latest_list= [] 
    conn = sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
    c = conn.cursor()
    sql = 'SELECT City.name FROM City'
    for row in c.execute(sql):
        latest_list.append(row)
    conn.close()
    context = {'list': latest_list}
    htmlResponse=json.dumps({'list':latest_list})
    return HttpResponse(htmlResponse)


def getSingleData(request):
    name=request.GET.get('name', '') #parameters name=city, otherwise ''
    dT=request.GET.get('dt','')
    #if (dT or name) == null: return HttpResponse('Error params!')
    latest_list= [] 
    conn = sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
    c = conn.cursor()
    sql = 'SELECT City.id,"%s".name,"%s".detection_time,'\
    'City.lat,City.lon,"%s".temp,"%s".humidity,"%s".wind_speed '\
    'FROM "%s",City WHERE City.name="%s".name AND date("%s".detection_time)=%s'%(name,name,name,name,name,name,name,name,dT)
    for row in c.execute(sql):
        latest_list.append(row)
    conn.close()
    context = {'list': latest_list}
    htmlResponse=json.dumps({'list':latest_list})
    return HttpResponse(htmlResponse)
    #return render(request,'weather/data_history.html',context)


def getLastTempData(request):
    name=request.GET.get('name', '') #parameters name=city, otherwise ''
    #if (dT or name) == null: return HttpResponse('Error params!')
    latest_list= [] 
    conn = sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
    c = conn.cursor()
    sql = 'SELECT "%s".name,"%s".detection_time,'\
    '"%s".temp '\
    'FROM "%s",City WHERE City.name="%s".name AND "%s".rowid = (SELECT MAX(rowid) FROM "%s")'%(name,name,name,name,name,name,name)
    for row in c.execute(sql):
        latest_list.append(row)
    conn.close()
    context = {'list': latest_list}
    htmlResponse=json.dumps({'list':latest_list})
    return HttpResponse(htmlResponse)


def getLastHumyData(request):
    name=request.GET.get('name', '') #parameters name=city, otherwise ''
    #if (dT or name) == null: return HttpResponse('Error params!')
    latest_list= [] 
    conn = sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
    c = conn.cursor()
    sql = 'SELECT "%s".name,"%s".detection_time,'\
    '"%s".humidity '\
    'FROM "%s",City WHERE City.name="%s".name AND "%s".rowid = (SELECT MAX(rowid) FROM "%s")'%(name,name,name,name,name,name,name)
    for row in c.execute(sql):
        latest_list.append(row)
    conn.close()
    context = {'list': latest_list}
    htmlResponse=json.dumps({'list':latest_list})
    return HttpResponse(htmlResponse)


def getLastPressure(request):
    name=request.GET.get('name', '') #parameters name=city, otherwise ''
    #if (dT or name) == null: return HttpResponse('Error params!')
    latest_list= [] 
    conn = sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
    c = conn.cursor()
    sql = 'SELECT "%s".detection_time,'\
    '"%s".pressure '\
    'FROM "%s" WHERE "%s".rowid = (SELECT MAX(rowid) FROM "%s")'%(name,name,name,name,name)
    for row in c.execute(sql):
        latest_list.append(row)
    conn.close()
    context = {'list': latest_list}
    htmlResponse=json.dumps({'list':latest_list})
    return HttpResponse(htmlResponse)


def learn(request):
    return render(request,'weather/learn.html')


def join_telegram(request):
    if request.user.is_authenticated():
        return render(request,'weather/joinTelegram.html')
    else:
        return HttpResponse("Before, you have to LogIn")


def signup(request):
    if request.method == 'POST': #after submit in html file, i get data from form and commit object
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = MyRegistrationForm()
    return render(request, 'weather/signup.html', {'form': form})



#This function creates multiple stations for any users. They are linked to a single account.
#You delete field called "name" in all city table, because it creates redundancy . Remember it!
def signup_weather(request):
    if request.user.is_authenticated():
        if request.method == 'POST': #after submit in html file, i get data from form and commit object
            mashup=str(request.user)+"_"+str(request.POST.get("weather_id")+"_"+str(request.POST.get("name")))
            conn = sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
            c = conn.cursor()
            sql = 'CREATE TABLE IF NOT EXISTS "%s" ("weather_id"  VARCHAR PRIMARY KEY NOT NULL ); '\
            'INSERT or IGNORE INTO "%s" VALUES ("%s"); '\
            'INSERT or IGNORE INTO City  VALUES ("%s","%s",%f,%f); '\
            'CREATE TABLE IF NOT EXISTS  "%s" ("name" VARCHAR , "temp" FLOAT, "humidity" FLOAT, "wind_speed" FLOAT, ' \
            '"detection_time" DATETIME PRIMARY KEY, "pressure" FLOAT, "wind_deg" FLOAT);' %(request.user,request.user,request.POST.get("weather_id"),
                                                                                            request.POST.get("weather_id"),mashup,
                                                                                            float(request.POST.get("latitude")),float(request.POST.get("longitude")),
                                                                                            mashup)
            c.executescript(sql)
            conn.commit()
            conn.close()            
            return redirect('/')
        else:
            form = SignUpWeatherForm(request=request.user)
            return render(request, 'weather/signup_weather.html', {'form': form})
    else:
        return HttpResponse("Before, You have to log in!")
     
    
def DataFromWs(request):
        data=request.GET.get('data', '') #parameters name=...., otherwise ''
        print(data)
        return HttpResponse(status=204)
    
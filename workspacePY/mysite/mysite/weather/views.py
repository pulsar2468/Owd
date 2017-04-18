from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import request
import sys
import sqlite3
import json
# Create your views here.


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
    sys.path.insert(0, "/home/nataraja/Scrivania/OpenData")
    import onOpenStreetMap
    onOpenStreetMap.real_time()
    HtmlFile = open('/home/nataraja/Scrivania/OpenData/workspacePY/real_timeMap.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    return HttpResponse(source_code)


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
    'FROM "%s",City WHERE City.name="%s".name AND "%s".detection_time=%s'%(name,name,name,name,name,name,name,name,dT)
    for row in c.execute(sql):
        latest_list.append(row)
    conn.close()
    context = {'list': latest_list}
    htmlResponse=json.dumps({'list':latest_list})
    return HttpResponse(htmlResponse)
    #return render(request,'weather/data_history.html',context)






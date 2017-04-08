from django.shortcuts import render
from django.http import HttpResponse
from django.template.context_processors import request
import sys
import sqlite3

# Create your views here.
def weather_test(request):
    return HttpResponse("Test Success")


def index(request):
    return render(request, 'weather/index.html') #he renders the template and the data with request http

def get_result(request):
    sys.path.insert(0, "/home/nataraja/Scrivania/OpenData")
    #import onOpenStreetMap
    #import owm_test
    HtmlFile = open('/home/nataraja/Scrivania/OpenData/workspacePY/mthood.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    return HttpResponse(source_code)





def history(request):
    latest_list= [] 
    conn = sqlite3.connect('/home/nataraja/Scrivania/db_weather.sqlite')
    c = conn.cursor()
    sql = 'SELECT City.id,Palermo.name,Palermo.detection_time,City.lat,City.lon,Palermo.temp,Palermo.humidity,Palermo.wind_speed FROM Palermo,City WHERE City.name=Palermo.name'
    for row in c.execute(sql):
        latest_list.append(row)
    conn.close()
    context = {'list': latest_list}
    return render(request, 'weather/data_history.html',context) #he renders the template and the data with request http
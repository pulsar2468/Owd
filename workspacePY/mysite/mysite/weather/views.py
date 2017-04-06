from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template.context_processors import request
import sys


 
#from .models import Question

# Create your views here.
def weather_test(request):
    return HttpResponse("Test Success")


def index(request):
    latest_question_list= [] 
    latest_question_list.append("hello")
    latest_question_list.append("world")
    context = {'latest_question_list': latest_question_list}
    return render(request, 'weather/index.html', context) #he renders the template and the data with request http

def get_result(request):
    sys.path.insert(0, "/home/nataraja/Scrivania/OpenData")
    import onOpenStreetMap
    import owm_test
    HtmlFile = open('/home/nataraja/Scrivania/OpenData/workspacePY/mthood.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    return HttpResponse(source_code)
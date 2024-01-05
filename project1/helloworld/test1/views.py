from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1 align=center><font color=red>Institute of Science and Information Technology</font></h1>")
# Create your views here.

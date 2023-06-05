from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    res=HttpResponse("""<html><body bgcolor=pink><h1><center>WELCOME  TO   GANESH PROJECT</center></h1></body></html>""")
    return res
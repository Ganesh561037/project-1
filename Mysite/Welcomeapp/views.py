from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def home(request):
    res=HttpResponse("""<html>
    <body bgcolor=green>
    <h1><center>Welcome TO NEW WORLD GANA</center></h1>
    </body>
    </html>""")
    return res

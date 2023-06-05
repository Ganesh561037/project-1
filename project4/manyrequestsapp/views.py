from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return  render(request,'home.html')
def getinput(request):
    return render(request,'getinput.html')
def postinput(request):
    return render(request,'postinput.html')
def add(request):
    if request.method=="GET":
        p=int(request.GET["G1"])
        q=int(request.GET["G2"])
        r=p+q
        return HttpResponse("THE SUM IS: "+str(r))
    else:
        x=int(request.POST["S1"])
        y=int(request.POST["S2"])
        z=x+y
        return HttpResponse("The Sum is: "+str(z))
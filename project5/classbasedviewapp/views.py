from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class Getinput(View):
    def get(self,request):
        return render(request,'getinput.html')
class Postinput(View):
    def get(self,request):
        return render(request,'postinput.html')
class Add(View):
    def get(self,request):
        p=int(request.GET["G1"])
        q=int(request.GET["G2"])
        r=p+q
        return HttpResponse("The sum is :"+str(r))
    def post(self,request):
        x=int(request.POST["S1"])
        y=int(request.POST["S2"])
        z=x+y
        return HttpResponse("The Sum Is : "+str(z))
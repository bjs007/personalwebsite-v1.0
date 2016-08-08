from django.shortcuts import render
def index(request):
    return render(request,'personal/home.html')
def contact(request):
    return render(request, 'personal/basic.html',{'content':['if you like to contact me, please email me','bijays.nitdgp@gmail.com']})
# Create your views here.

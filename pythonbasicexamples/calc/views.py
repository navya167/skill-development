from django.shortcuts import render

# Create your views here.
def greeting(request):
    return render(request,'calculator.html',{'name':'Welcome to Django'});


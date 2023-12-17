from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    return  render(request,"index.html")


def addition(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    res = x + y
    p = x - y
    k = x / y
    t = x * y

    return render(request, "about.html", {'result': res,'result1':p,'result2':k,'result3':t})

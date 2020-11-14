from django.shortcuts import render
from django.http import HttpResponse

def DashboardHome(request):
        # return HttpResponse('<h2>Hello World</h2>')
    return render(request, 'dashboard/base.html')
# Create your views here.

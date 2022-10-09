from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render

def mainpage(request):
    return render(request, 'mainpage.html')
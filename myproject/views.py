# from django.http import HttpResponse 
from django.shortcuts import render

def homepage(request):
  #  return HttpResponse("This is a demo website by Muyonjo Paul.")
    return render(request, 'home.html')

def The_why(request):
   # return HttpResponse("I thought i could do it so i did it.")
   return render(request, 'The_why.html')
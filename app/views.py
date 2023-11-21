from django.shortcuts import render

# Create your views here.


def forloop (request):
    d={'name':'lakshmi'}
    return render(request,'forloop.html',d)



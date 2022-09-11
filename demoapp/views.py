from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from demoapp.models import place, news


def fun(request):
    obj = place.objects.all()
    objs = news.objects.all()
    return render(request, "index.html", {'result': obj, 'res': objs})

"""
def add(request):
    a = (request.POST["m"])
    return render(request, "nextpage.html", {'ad': a})  """

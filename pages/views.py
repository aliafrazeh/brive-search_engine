from django.shortcuts import render
from .models import serachArticle
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request,"pages/home.html")

def search(request):
    if request.method == "GET":
        searched = request.GET['searched']
        article = serachArticle.objects.filter(Q(titlesearceh__icontains=searched,status=True))
        return render(request,'pages/search.html',{"searched":searched,'article':article})
    else:
        return render(request,'pages/home.html')


def license_view(request):
    return render(request,'pages/license.html')

def programmer(request):
    return render(request,'pages/programmer.html')
    
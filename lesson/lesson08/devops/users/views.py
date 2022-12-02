from django.shortcuts import render

# Create your views here.


def listView(request):
    return render(request,"assets/list.html")
from django.shortcuts import render

# Create your views here.


def home(request):
    data = "hello www"
    return render(request, "app/home.html", {"data": data})

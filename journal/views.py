from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html", content_type="text/html")

from django.shortcuts import render

# Create your views here.

def index(request):
    if request.user.is_authenticated():
        return render(request, "index_loggedin.html")
    return render(request, "index_public.html")

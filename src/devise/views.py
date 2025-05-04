from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, "devise/index.html", context={"liste_nombre": range(15)})
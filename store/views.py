from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Load the html
def index(request):

    # REMINDER : when using render(), don't forget to include current app on settings.py
    # for further instructions on adding apps, proceed to settings.py 
    return render(request, 'store/index.html')

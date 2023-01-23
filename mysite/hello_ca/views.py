from django.shortcuts import render
from .models import Employee
# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {"employees":[]}
    return render(request, 'hello_ca/index.html', context)

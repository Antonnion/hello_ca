from django.shortcuts import render
from .models import Employee
# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {
        "employees": [
            Employee(name="kei", intro_text="I am kei."),
            Employee(name="masahiro", intro_text="I am masahiro.")
        ]
    }
    return render(request, 'hello_ca/index.html', context)

def upload(request):
    return render(request, 'hello_ca/upload.html')
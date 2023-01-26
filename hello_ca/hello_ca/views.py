from django.shortcuts import render
from django.views import generic
from django.http import HttpRequest

from .models import Employee
from . import models


class ListView(generic.ListView):
    template_name = "hello_ca/index.html"
    context_object_name = "employees"

    def get_queryset(self):
        return Employee.objects.all()[:5]


def upload(request: HttpRequest):
    if request.method == "POST":
        model = models.EmployeeForm(request.POST)
        model.save()
        return render(request, 'hello_ca/upload.html')
    return render(request, 'hello_ca/upload.html')

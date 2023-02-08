from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from . import models


class ListView(generic.ListView):
    template_name = "hello_ca/index.html"
    context_object_name = "employees"

    def get_queryset(self):
        return models.Employee.objects.all()[:8]


def detail(request: HttpRequest, pk: int):
    if request.method == "POST":
        employee = get_object_or_404(models.Employee, pk=pk)
        employee.delete()
        return redirect("index")
    employee = models.Employee.objects.get(pk=pk)
    return render(request, "hello_ca/detail.html", {"employee": employee})


def upload(request: HttpRequest):
    if request.method == "POST":
        model = models.EmployeeForm(request.POST)
        model.save()
        return render(request, 'hello_ca/upload.html')
    depertments = models.Depertment.objects.all()
    return render(request, 'hello_ca/upload.html', {
        "depertments": depertments
    })

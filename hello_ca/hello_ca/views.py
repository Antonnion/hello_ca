from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic

from . import models


def index(request: HttpRequest):
    # TODO: employeesが0のときの例外処理が欲しい．
    return render(request, "hello_ca/index.html", {
        "employees": models.Employee.objects.all()[:8],
        "depertments": models.Depertment.objects.all()
    })


def detail(request: HttpRequest, pk: int):
    employee = get_object_or_404(models.Employee, pk=pk)
    if request.method == "POST":
        employee.delete()
        return redirect("index")
    return render(request, "hello_ca/detail.html", {"employee": employee})


def upload(request: HttpRequest):
    if request.method == "POST":
        model_form = models.EmployeeForm(request.POST)
        model_form.save()
        return render(request, 'hello_ca/upload.html')
    depertments = models.Depertment.objects.all()
    return render(request, 'hello_ca/upload.html', {
        "depertments": depertments
    })


def edit(request: HttpRequest, pk: int):
    employee = get_object_or_404(models.Employee, pk=pk)
    if request.method == "POST":
        model_form = models.EmployeeForm(request.POST, instance=employee)
        if model_form.is_valid():
            model_form.save()
            return redirect("detail", pk=pk)
    depertments = models.Depertment.objects.all()
    return render(request, 'hello_ca/edit.html', {
        "employee": employee,
        "depertments": depertments
    })

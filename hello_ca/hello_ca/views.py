from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q

from . import models


DISPLAY_EMPLOYEE_COUNT = 8


def index(request: HttpRequest):
    if len(request.GET):
        search_name = request.GET["search_name"]
        employees = models.Employee.objects.filter(
            Q(first_name__icontains=search_name)
            | Q(last_name__icontains=search_name)
            | Q(first_name_kana__icontains=search_name)
            | Q(last_name_kana__icontains=search_name)
        )[:DISPLAY_EMPLOYEE_COUNT]
    else:
        employees = models.Employee.objects.all()[:DISPLAY_EMPLOYEE_COUNT]

    # TODO: employeesが0のときの例外処理が欲しい．
    return render(request, "hello_ca/index.html", {
        "employees": employees,
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

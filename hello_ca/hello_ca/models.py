from django.db import models
from django.forms import ModelForm


class Department(models.Model):
    name = models.CharField(max_length=64)


class DepartmentFrom(ModelForm):
    class Meta:
        model = Department
        fields = ["name"]


class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, null=True)
    first_name_kana = models.CharField(max_length=64, null=True)
    last_name_kana = models.CharField(max_length=64, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=True, blank=True)
    intro_text = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.first_name


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = [
            "first_name", "last_name", "first_name_kana", "last_name_kana",
            "department", "intro_text"
        ]

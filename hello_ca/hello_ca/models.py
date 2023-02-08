from django.db import models
from django.forms import ModelForm


class Depertment(models.Model):
    name = models.CharField(max_length=64)
    short_name = models.CharField(max_length=8)


class Employee(models.Model):
    name = models.CharField(max_length=64)
    depertment = models.ForeignKey(
        Depertment, on_delete=models.CASCADE, null=True, blank=True)
    intro_text = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["name", "intro_text"]

from django.db import models
from django.forms import ModelForm


class Employee(models.Model):
    name = models.CharField(max_length=50)
    intro_text = models.CharField(max_length=256)

    # def __init__(self, name, intro_text):
    #     self.name = name
    #     self.intro_text = intro_text

    def __str__(self) -> str:
        return self.name


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["name", "intro_text"]

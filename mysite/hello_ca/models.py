from django.db import models

# Create your models here.
class Employee:
    def employee(self, employee_name, employee_intro_text, employee_image):
        self.name = employee_name
        self.intro = employee_intro_text
        self.image = employee_image
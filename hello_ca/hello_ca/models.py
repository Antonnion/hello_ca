from django.db import models

# Create your models here.
class Employee:
    # def __init__(self, employee_name, employee_intro_text, employee_image):
    def __init__(self, name, intro_text):
        self.name = name
        self.intro_text = intro_text
        # self.image = image
from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    intro_text = models.CharField(max_length=256)

    def __init__(self, name, intro_text):
        self.name = name
        self.intro_text = intro_text
        # self.image = image
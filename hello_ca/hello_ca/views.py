from django.shortcuts import render
from django.views import generic

from .models import Employee


class IndexView(generic.ListView):
    template_name = "hello_ca/index.html"
    context_object_name = "employees"

    def get_queryset(self):
        return [
            Employee(name="kei", intro_text="I am kei."),
            Employee(name="masahiro", intro_text="I am masahiro.")
        ]


def upload(request):
    if request.method == "POST":
        name = request.POST["name"]
        intro_text = request.POST["intro_text"]
    return render(request, 'hello_ca/upload.html')

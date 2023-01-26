from django.urls import path

from . import views


urlpatterns = [
    path('', views.ListView.as_view(), name='index'),
    path('upload/', views.upload, name='upload')
]

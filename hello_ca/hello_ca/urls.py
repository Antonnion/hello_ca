from django.urls import path

from . import views


urlpatterns = [
    path('', views.ListView.as_view(), name='index'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('upload/', views.upload, name='upload'),
]

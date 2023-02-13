from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:page>/', views.index, name='index'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('upload/', views.upload, name='upload'),
    path('edit/<int:pk>/', views.edit, name='edit')
]

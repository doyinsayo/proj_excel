from django.urls import path

from . import views

app_name = "my_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.file_2, name='file-2')
]
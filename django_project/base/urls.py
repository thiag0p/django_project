from django.urls import path
from django_project.base.views import home

app_name = 'base'

urlpatterns = [
    path('', home, name='home'),
]

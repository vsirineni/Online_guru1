
from . import views
from django.urls import path

app_name = 'hobbies'
urlpatterns = [
    path('', views.hobby_list, name='hobby_list'),
    path('hobby_list', views.hobby_list, name='hobby_list'),


]
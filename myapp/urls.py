from django.contrib import admin
from django.urls import path,include
from myapp import views
urlpatterns = [
    path('',views.home,name="home"),
    path('new_search',views.newSearch,name="search"),
]
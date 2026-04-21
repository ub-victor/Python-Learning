from django.urls import path
from . import views # From the current folder import view file

#  /products
urlpatterns = [
    path('', views.index),
    path('/new', views.new),

]
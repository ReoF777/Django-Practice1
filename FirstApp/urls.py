from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('sum/<int:num1>/<int:num2>', views.add, name='add'),
    path('minus/<int:num1>/<int:num2>', views.minus, name='minus'),
    path('div/<int:num1>/<int:num2>', views.div, name='div'),
]
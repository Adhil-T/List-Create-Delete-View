from django.contrib import admin
from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('units/', views.UnitListView.as_view(),name='unit_list'),
]
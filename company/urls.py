from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.employees_list, name='employees_list'),
    path('employees/<int:id>/', views.employe_detail, name='employe_detail'),
    path('positions/', views.positions_list, name='positions_list'),
    path('subdivisions/', views.subdivisions_list, name='subdivisions_list'),
    path('departments/', views.departments_list, name='departments_list'),
    path('subdivisions/new/', views.subdivisions_new, name='subdivisions_new'),
    path('employees/new/', views.employees_new, name='employees_new'),
    path('employees/edit/<int:id>/', views.employe_edit, name='employe_edit'),
    path('subdivisions/delete/<int:id>/', views.subdivisions_delete, name='subdivisions_delete'),
    path('employees/delete/<int:id>/', views.employees_delete, name='employees_delete'),


]

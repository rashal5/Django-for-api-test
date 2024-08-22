from . import views
from django.urls import path

urlpatterns = [
    path('all',views.all_employee),
    path('check/<int:id>/',views.all_check),
    path('delete/<int:id>/',views.all_delete),
    path('create',views.employee_create),
    path('createser',views.employee_createuseingser),
    path('employee_update/<int:id>/',views.employee_update),
]
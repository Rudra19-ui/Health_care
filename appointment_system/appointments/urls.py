from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_appointment, name='schedule_appointment'),
    path('admin-view/', views.admin_view, name='admin_view'),
]

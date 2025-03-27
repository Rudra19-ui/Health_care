from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_appointment, name='schedule_appointment'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('ai-doctor-chatbot/', views.ai_doctor_chatbot, name='ai_doctor_chatbot'),
    path('doctors/', views.doctors_list, name='doctors_list'),  # Add this line
]
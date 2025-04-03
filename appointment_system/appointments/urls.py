from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_appointment, name='schedule_appointment'),
    path('admin-view/', views.admin_view, name='admin_view'),
<<<<<<< HEAD
    path('ai-doctor-chatbot/', views.ai_doctor_chatbot, name='ai_doctor_chatbot'),
    path('doctors/', views.doctors_list, name='doctors_list'),  # Add this line
]
=======
]
>>>>>>> cae47a086aed8325146460eb9077d1a42a3fb10b

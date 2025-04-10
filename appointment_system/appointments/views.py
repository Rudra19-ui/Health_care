from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Appointment
<<<<<<< HEAD
from .models import Doctor  
=======
>>>>>>> cae47a086aed8325146460eb9077d1a42a3fb10b


def schedule_appointment(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        service_type = request.POST.get('service-type')
        date = request.POST.get('date')

        # Save the appointment to the database
        try:
            Appointment.objects.create(
                name=name,
                phone=phone,
                city=city,
                service_type=service_type,
                date=date
            )
            # Custom success message
            return JsonResponse({'message': 'Your appointment has been successfully booked! We will contact you shortly.'})
        except Exception as e:
            # Custom error message
            return JsonResponse({'error': 'An error occurred while booking your appointment. Please try again later.'}, status=400)

    return render(request, 'appointments/schedule.html')

<<<<<<< HEAD

=======
>>>>>>> cae47a086aed8325146460eb9077d1a42a3fb10b
def admin_view(request):
    # Get all appointments grouped by service type
    appointments = {
        'Clinical Laboratory Test': Appointment.objects.filter(service_type='Clinical Laboratory Test'),
        'Vision Health Check': Appointment.objects.filter(service_type='Vision Health Check'),
        'Dermatological Skin Exam': Appointment.objects.filter(service_type='Dermatological Skin Exam'),
    }
    return render(request, 'appointments/admin.html', {'appointments': appointments})
<<<<<<< HEAD


def ai_doctor_chatbot(request):
    # Render the AI Doctor chatbot page
    return render(request, 'appointments/new_folder/chatbot/index1.html')

def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'appointments/new_folder/doctors.html', {'doctors': doctors})
=======
>>>>>>> cae47a086aed8325146460eb9077d1a42a3fb10b

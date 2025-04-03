from django.db import models

<<<<<<< HEAD
=======

>>>>>>> cae47a086aed8325146460eb9077d1a42a3fb10b
class Appointment(models.Model):
    SERVICE_CHOICES = [
        ('Clinical Laboratory Test', 'Clinical Laboratory Test'),
        ('Vision Health Check', 'Vision Health Check'),
        ('Dermatological Skin Exam', 'Dermatological Skin Exam'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.service_type}"
<<<<<<< HEAD


class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Neurology', 'Neurology'),
        ('Dermatology', 'Dermatology'),
        ('Pediatrics', 'Pediatrics'),
        ('Oncology', 'Oncology'),
    ]
    
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
    hospital = models.CharField(max_length=100)
    bio = models.TextField()
    contact = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='doctors/')
    available_days = models.CharField(max_length=100)
    available_time = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.name} - {self.specialization}"
=======
>>>>>>> cae47a086aed8325146460eb9077d1a42a3fb10b

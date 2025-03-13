from django.db import models


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

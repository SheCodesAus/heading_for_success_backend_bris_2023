from django.db import models
# from django.contrib.auth import get_user_model

# Create your models here.

class Program(models.Model):

    new = 'New'
    open = 'Open'
    closed = 'Closed'
    cancelled = 'Cancelled'

    STATUS_CHOICES = (
        (new, 'New'),
        (open, 'Open'),
        (closed, 'Closed'),
        (cancelled, 'Cancelled'),
    )    
    program_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    intake = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField()
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='New'
    )
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    application_date_start = models.DateTimeField()
    application_date_end = models.DateTimeField()
    

class Scholarship(models.Model):
    organization = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200)
    contact_email = models.EmailField()
    contact_mobile = models.IntegerField()
    scholarship_amount = models.IntegerField()
    number_available = models.IntegerField()
    program = models.ForeignKey(
        'Program',
        on_delete=models.CASCADE,
        related_name='scholarship'
    )
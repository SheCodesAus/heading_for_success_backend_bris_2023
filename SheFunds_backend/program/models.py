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

    brisbane = 'Brisbane'
    sydney = 'Sydney'
    melbourne = 'Melbourne'
    perth = 'Perth'
    canberra = 'Canberra'
    darwin = 'Darwin'   
    tasmania = 'Tasmania' 

    LOCATION_CHOICES = (
        (brisbane, 'Brisbane'),
        (sydney, 'Sydney'),
        (melbourne, 'Melbourne'),
        (perth, 'Perth'),
        (canberra, 'Canberra'),
        (darwin, 'Darwin'),
        (tasmania, 'Tasmania'),        
    )   

    program_name = models.CharField(max_length=200)
    location = models.CharField(
        max_length=20, 
        choices=LOCATION_CHOICES, 
    )
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

class Applicant(models.Model):

    brisbane = 'Brisbane'
    sydney = 'Sydney'
    melbourne = 'Melbourne'
    perth = 'Perth'
    canberra = 'Canberra'
    darwin = 'Darwin'   
    tasmania = 'Tasmania' 

    LOCATION_CHOICES = (
        (brisbane, 'Brisbane'),
        (sydney, 'Sydney'),
        (melbourne, 'Melbourne'),
        (perth, 'Perth'),
        (canberra, 'Canberra'),
        (darwin, 'Darwin'),
        (tasmania, 'Tasmania'),        
    )   

    new = 'New'
    shortlist = 'Shortlist'
    interview = 'Interview'
    rejected = 'Rejected'
    withdrawn = 'Withdrawn'
    successful = 'Successful'
    scholarship = 'Scholarship Assigned'    

    STATUS_APPLICANT_CHOICES = (
        (new, 'New'),
        (shortlist, 'Shortlist'),
        (interview, 'Interview'),
        (rejected, 'Rejected'),
        (withdrawn, 'Withdrawn'),
        (successful, 'Successful'),
        (scholarship, 'Scholarship Assigned'),
    )       

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField()
    contact_mobile = models.IntegerField()
    location =  models.CharField(
        max_length=20, 
        choices=LOCATION_CHOICES, 
    )
    reason = models.TextField()
    previous_education = models.CharField(max_length=200)
    work_experience = models.TextField()
    currently_employed = models.BooleanField()
    # current_employer = models.CharField(max_length=200, blank=True)    
    current_employer = models.CharField(max_length=200)    
    biography = models.TextField()
    gender_eligible = models.BooleanField()
    # resume = models.URLField(blank=True)
    resume = models.URLField()
    status = models.CharField(
        max_length=20, 
        choices=STATUS_APPLICANT_CHOICES, 
        default='New'
    )
    program = models.ForeignKey(
        'Program',
        on_delete=models.CASCADE,
        related_name='applicant'
    )
    scholarship = models.ForeignKey(
        'Scholarship',
        on_delete=models.CASCADE,
        related_name='assigned_scholarship',
        null=True,
        blank=True
    )    
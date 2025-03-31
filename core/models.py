from django.db import models
from django.core.validators import RegexValidator, EmailValidator
from django.utils.timezone import localtime
from django.utils.translation import gettext_lazy as _

# Create your models here.
class SolarInquiry(models.Model):
    """Enchanced model with advanced validation"""
    PROPERTY_CHOICES = [
        ('residential', _('Residential')),
        ('commercial', _('Commercial')),
        ('industrial', _('Industrial')),
    ]
    
    name = models.CharField(
        max_length=200,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]{2,}$',
                message=_("Name must be at least 2 characters long and contain only letters")
            )
        ]
    )
    
    
    email = models.EmailField(
        validators=[EmailValidator(message=_("Email a valid email address"))]
    )
    
    
    phone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message=_("Enter a valid phone number")
            )
        ]
    )
    
    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_CHOICES,
        default='residential'
    )
    current_energy_usage = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=_("Enter your current energy usage in kWh")
    )
    
    additional_notes = models.TextField(blank=True, null=True)
        
    create_at = models.DateTimeField(auto_now_add=True)
    
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        formatted_date = localtime(self.create_at).strftime('%Y-%m-%d %H:%M:%S')
        return f"{self.name} - Solar Inquiry on {formatted_date}"
    
   
   
    
    # About Contact Form


class BusinessContactMessage(models.Model):
    PROPERTY_CHOICES = [
        ('residential', 'Residential'),
        ('commercial', 'Commercial'),
        ('farm', 'Farm/Agricultural'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    property_type = models.CharField(max_length=20, choices=PROPERTY_CHOICES)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.email} - {self.created_at.strftime('%Y-%m-%d')}"
    
    

class GeneralContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name}"
    
    # New contact
class GeneralSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.name} - {self.email}"
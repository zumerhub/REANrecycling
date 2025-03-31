from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import SolarInquiry

@receiver(post_save, sender=SolarInquiry)
def send_inquiry_email(sender, instance, created, **kwargs):
    """Send email notification for new inquiry"""
    if created:
        subject = f"New Solar Inquiry from {instance.name}"
        message = (
            f"Hi {instance.name},\n\n"
            f"Thank you for your interest in solar energy. We have received your inquiry and will get back to you shortly.\n\n"
            f"New Solar Inquiry Details:\n"
            f"Name: {instance.name}\n"
            f"Email: {instance.email}\n"
            f"Phone: {instance.phone}\n"
            f"Property Type: {getattr(instance, 'property_type', 'N/A')}\n"
            f"Additional Notes: {instance.additional_notes or 'None'}\n\n"
        )
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )
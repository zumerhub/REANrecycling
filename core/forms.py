from django import forms
from django.forms import ModelForm
# from django.core.exceptions import ValidationError
from .models import GeneralContactMessage, BusinessContactMessage




# New general contact
class GeneralForm(forms.ModelForm):
    class Meta:
        model = GeneralContactMessage
        fields = ['name', 'email', 'phone', 'message']
   
    
class BusinessContactForm(forms.ModelForm):
    class Meta:
        model = BusinessContactMessage
        fields = ['name', 'email', 'phone', 'property_type', 'message']
    
    
    
    
    
    

# class SolarInquiryForm(forms.ModelForm):
#     """Advanced form validation and error handling."""
#     def clean_current_energy_usage(self):
#         """Custom validation for energy usage"""
#         energy_usage = self.cleaned_data.get('current_energy_usage')
#         if energy_usage is not None and energy_usage < 0:
#             raise ValidationError("Energy usage cannot be negative")
        
#         if energy_usage is not None and energy_usage > 1000:
#             raise ValidationError("Energy usage cannot be more than 1000")
        
#         return energy_usage
    
    # def clean(self):
    #     """Perform additional cross-field validation for form data"""
    #     cleaned_data = super().clean()
    #     name = cleaned_data.get('name')
    #     email = cleaned_data.get('email')
        
    #     # Prevent generic emails from being sent
    #     if email and any(domain in email for domain in ['gmail.com', 'yahoo.com', 'hotmail.com']) and not name:
    #         self.add_error('name', 'Please provide your name')
    #         self.add_error('email', 'Please use a valid email address')
            
    #     return cleaned_data
    
    # class Meta:
    #     model = SolarInquiry
    #     fields = ['name', 'email', 'phone', 'current_energy_usage', 'property_type', 'additional_notes']

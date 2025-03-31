# from django.contrib import admin
# from .models import ContactMessage, GeneralContactMessage

# # Register your models here.
# admin.site.register(ContactMessage)
# admin.site.register(GeneralContactMessage)


from django.contrib import admin
from .models import BusinessContactMessage, GeneralContactMessage


@admin.register(GeneralContactMessage)
class GeneralContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)



@admin.register(BusinessContactMessage)
class BusinessContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'property_type', 'message', 'created_at')
    search_fields = ('name', 'email', 'phone')
    
    
# @admin.register(GeneralSubmission)
# class GeneralSubmissionAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'phone', 'created_at')
#     search_fields = ('name', 'email')
#     list_filter = ('created_at',)


from django.urls import path
from .import views
from .views import initiate_payment, payment_webhook


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

    # business contact form (API) 
    path('api/business/contact/', views.business_contact_view, name='business_contact_view'),
    # ... general form (APIs) URLs
    path('api/general/', views.general_view, name='general_view'),

    # ... payment (APIs) URLs
    path('api/initiate-payment/', initiate_payment, name='initiate_payment'),
    path('api/payment/webhook/', payment_webhook, name='payment_webhook'),
]


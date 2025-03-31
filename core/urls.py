

from django.urls import path
from .import views
from .views import initiate_payment, payment_webhook


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    # path('home/', views.home, name='home'),

    # contact api
    path('api/business/contact/', views.business_contact_view, name='business_contact_view'),
    # path('api/general/contact/', views.general_contact_view, name='general_contact_view'),

    # ... general (APIs) URLs
    path('api/general/', views.general_view, name='general_view'),

    # ... payment (APIs) URLs
    path('api/initiate-payment/', initiate_payment, name='initiate_payment'),
    path('api/payment/webhook/', payment_webhook, name='payment_webhook'),

    # path('payment/', views.paystack_payment, name='paystack_payment'),
    # path('payment/success/', views.payment_success, name='payment_success'),
]


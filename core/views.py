from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings
from .models import BusinessContactMessage
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .paystack import PaystackTransaction
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
import logging
from .forms import generalContactForm, GeneralForm


# import stripe


# Create your views here.

# Set up logging
logger = logging.getLogger(__name__)


@csrf_exempt
def general_view(request):
    try:      
        if request.method == 'POST':
            form = GeneralForm(request.POST)
            if form.is_valid():
                form.save()
                # messages.success(request, 'Your message has been sent successfully.')
                # return redirect('home')
                return JsonResponse({'status':  'success'})
            else:
                return JsonResponse({'status': 'error','errors': form.errors}, status=400)
        else:
            form = GeneralForm()
        # return render(request, 'core/general_home.html', {'form': form})
    except Exception as e:
        print(f"ERROR: {str(e)}")
        return JsonResponse({'status': 'error','errors': str(e)}, status=500)
    

# Stripe API Key
# stripe.api_key = settings.STRIPE_SECRET_KEY


# Stripe API
# def payment_view(request):
#         """Stripe payment integration view"""
#         if request.method == 'POST':
#             try:
#                 checkout_session = stripe.checkout.Session.create(
#                     payment_method_types=['card'],
#                     line_items=[{
#                         'price_data': {
#                             'currency': 'usd',
#                             'unit_amount': 2000, # default price in cents
#                             'product_data': {
#                                 'name': 'Solar Panel Installation',
#                             },
#                         },
#                         'quantity': 1,
#                     }],
#                     mode='payment',
#                     success_url=request.build_absolute_uri('/payment/success/'),
#                     cancel_url=request.build_absolute_uri('/payment/cancel/'),
#                 )
#                 return redirect(checkout_session.url, code=303)
#             except Exception as e:
#                 return render(request, 'core/payment.html', {'error': str(e)})
        
#         return render(request, 'core/payment.html', {
#             'public_key': settings.STRIPE_PUBLIC_KEY,
#         })


# Make payment
# def paystack_payment(request):
#     """PayStack Payment Integration"""                                                                      
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         amount = int(request.POST.get('amount')) * 100
    
#     # Initialize transaction
#         headers = {
#             'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}',
#             'Content-Type': 'application/json',
#         }
#         data = {
#             'email': email,
#             'amount': amount,
#             'callback_url': request.build_absolute_uri('/payment/success/'),
#         }
#         response = requests.post('https://api.paystack.co/transactions/initialize', json=data, headers=headers)
#         response_data = response.json()
        
#         if response_data.get('status'):
#             # Redirect to paystack payment page
#             return redirect(response_data['data']['authorization_url'])
#         else:
#             # Handle error
#             return render(request, 'core/payment.html', {'error': response_data.get('message')})
    
#     return render(request, 'core/payment.html', {
#         'public_key': settings.PAYSTACK_PUBLIC_KEY,
#     })
    
    
# Verify payment
# def payment_success(request):
#     """Handle sucessful payment"""
#     reference = request.GET.get('reference')
    
#     # Verify transaction
#     headers = {
#         'Authorization': f'Bearer {settings.PAYSTACK_SECRET_KEY}'
#     }
#     response = request.get(f'https://api.paystack.co/transaction/verify{reference}', headers=headers)
#     response_data = response.json()
    
#     if response_data.get('status') and response_data['data']['status'] == 'success':
#         # Payment was successful
#         return render(request, 'core/success.html', {'transaction': response_data['data']})
#     else:
#         # Payment failed
#         return render(request, 'core/failure.html', {'error': response_data.get('message')})
    
# def home(request):
#     """Main landing page with inquiry form"""
#     if request.method == 'POST':
#         form = SolarInquiryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your inquiry has been submitted successfully')
#             return redirect('home')
#     else:
#         form = SolarInquiryForm()
#     return render(request, 'core/home.html', {'form': form, 'title': 'home'})
#     # return render(request, 'core/home.html')

def index(request):
    """Main landing page with inquiry form"""
   
    form = generalContactForm()  # The form is inside the Herosection 
    return render(request, 'core/index.html', {'form': form, 'title': 'Mainpage'})

def about(request):
    """About page with business information"""
    return render(request, 'core/about.html', {'title': 'About Us'})

def general_contact_view(request):
    """Hero section Form handler"""
    if request.method == 'POST':
        form = generalContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Your message has been received!'})
        else:
            return JsonResponse({'success': False, 'error': 'Invalid form submission', 'details': form.errors}, status=400)
    
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)


# Check site with SEO search
def robots_txt(request):
    content = """User-Agent: *
Disallow: /admin/
Disallow: /private/
Allow: /
Sitemap: https://127.0.0.1:8000/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")



# Paystack integration
@csrf_exempt
@require_http_methods(["POST"])
def initiate_payment(request):
    """
    Endpoint to initialize Paystack payment
    """
    try:
        # Parse JSON data from request body
        data = json.loads(request.body)
        amount = float(data.get('amount'))
        email = data.get('email')

        # Validate input
        if not amount or not email:
            return JsonResponse({
                'status': 'error',
                'message': 'Amount and email are required'
            }, status=400)

        # Create Paystack transaction
        paystack = PaystackTransaction()
        response = paystack.initialize_transaction(
            amount=amount, 
            email=email, 
            callback_url='https://yourwebsite.com/payment/callback'
        )

        # Check Paystack response
        if response.get('status') and response.get('data'):
            return JsonResponse({
                'status': 'success',
                'authorization_url': response['data']['authorization_url'],
                'reference': response['data']['reference']
            })
        else:
            return JsonResponse({
                'status': 'error',
                'message': response.get('message', 'Payment initialization failed')
            }, status=400)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def payment_webhook(request):
    """
    Webhook to handle Paystack payment callbacks
    """
    try:
        # Parse incoming webhook data
        payload = json.loads(request.body)
        
        # Verify the transaction
        paystack = PaystackTransaction()
        verification = paystack.verify_transaction(payload.get('reference'))

        if verification.get('status') and verification['data']['status'] == 'success':
            # Payment successful - update your database
            # Example: 
            # update_payment_status(
            #     reference=payload.get('reference'),
            #     status='successful',
            #     amount=verification['data']['amount'] / 100  # Convert back to naira
            # )
            return JsonResponse({'status': 'success'})
        else:
            # Payment failed
            return JsonResponse({'status': 'failed'}, status=400)

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)
        
        
# @require_POST
# @csrf_exempt
# def business_contact_view(request):
#     print(f"Content-Type: {request.content_type}")
#     print(f"Request Body: {request.body}")

#     try:
#         if request.content_type == "application/json" and request.body:
#             data = json.loads(request.body)
#             print(f"Parsed data: {data}")
#         else:
#             return JsonResponse({
#                 'success': False,
#                 'error': 'Invalid request format. Expected JSON.'
#             }, status=400)

#         # Extract the required fields from the JSON data
#         name = data.get('name', '').strip()
#         email = data.get('email', '').strip()
#         phone = data.get('phone', '').strip()
#         property_type = data.get('property', '').strip()
#         messages = data.get('message', '').strip()

#         # Validate the input data
#         if not name or not email or not messages:
#             return JsonResponse({
#                 'success': False,
#                 'error': 'Name, email, and message are required fields.'
#             }, status=400)

#         # Save to Database
#         contact = BusinessContactMessage.objects.create(
#             name=name,
#             email=email,
#             phone=phone,
#             property_type=property_type,
#             message=messages,
#         )
        
        
#         # Send the email notification
#         # email_subject = f"New contact form submission: {name}"
#         # email_message = (
#         #     f"New contact form submission received:\n\n"
#         #     f"Name: {name}\n"
#         #     f"Email: {email}\n"
#         #     f"Phone: {phone}\n"
#         #     f"property_type: {property_type}\n\n"
#         #     f"Message: {messages}\n"            
#         # )
        
#         # send_mail(
#         #     subject=email_subject,
#         #     message=email_message,
#         #     from_email=settings.DEFAULT_FROM_EMAIL,
#         #     recipient_list=[settings.CONTACT_FROM_RECIPIENTS],
#         #     fail_silently=False,
#         # )
        
#         # Return a success response
#         return JsonResponse({
#             'success': True,
#             'message': 'Your message has been received successfully'
#         })

#     except json.JSONDecodeError:
#         return JsonResponse({
#             'success': False,
#             'error': 'Invalid JSON data'
#         }, status=400)
    
#     except Exception as e:
#         print(f"Error Processing contact form: {str(e)}")
#         return JsonResponse({
#             'success': False,
#             'error': f'An error occurred while processing your message: {str(e)}'
#         }, status=500)
        

# @csrf_exempt  # Temporarily disable CSRF for testing (not recommended in production)
# def business_contact_view(request):
#     if request.method != "POST":
#         return JsonResponse({"error": "Only POST requests are allowed"}, status=405)

#        # Print request headers and body for debugging
#     print(f"Headers: {request.headers}")
#     print(f"Content-Type: {request.content_type}")
#     print(f"Raw Request Body: {request.body}")

#     # Ensure Content-Type is application/json
#     if request.content_type != "application/json":
#         return JsonResponse({"error": "Invalid Content-Type. Use application/json"}, status=400)

#     try:
#         data = json.loads(request.body)
#         print(f"Parsed data: {data}")  # Debugging output

#         # Extract and validate fields
#         name = data.get('name', '').strip()
#         email = data.get('email', '').strip()
#         phone = data.get('phone', '').strip()
#         property_type = data.get('property', '').strip()
#         messages = data.get('message', '').strip()

#         if not name or not email or not messages:
#             return JsonResponse({"error": "Name, email, and message are required"}, status=400)

#         # Save to database
#         contact = BusinessContactMessage.objects.create(
#             name=name,
#             email=email,
#             phone=phone,
#             property_type=property_type,
#             message=messages
#         )

#         return JsonResponse({"success": True, "message": "Message received successfully"}, status=201)

#     except json.JSONDecodeError:
#         return JsonResponse({"error": "Invalid JSON format"}, status=400)

#     except Exception as e:
#         print(f"Error: {e}")  # Debugging output
#         return JsonResponse({"error": "An error occurred while processing your message"}, status=500)
        
    
    
# @csrf_exempt  # Temporarily disable CSRF for testing (not recommended in production)
# def business_contact_view(request):
#     if request.method == 'POST':
#         try:
#             print(f"Raw Request Body: {request.body}")  # Print raw data
            
#             data = json.loads(request.body)
            
#             print(f"Parsed Data: {data}")  # Log parsed data

#             name = data.get('name', '')
#             email = data.get('email', '')
#             phone = data.get('phone', '')
#             property_type = data.get('property', '')
#             messages = data.get('message', '')

#             if not name or not email or not messages:
#                 return JsonResponse({'success': False, 'error': 'All fields are required'}, status=400)

#             # Save to database
#             contact = BusinessContactMessage.objects.create(
#                 name=name, email=email, phone=phone, property_type=property_type, message=messages
#             )
#             logger.info(f"Saved Contact: {contact}")

#             return JsonResponse({'success': True, 'message': 'Message received successfully'})


#         except Exception as e:
#             logger.error(f"Failed to save: {str(e)}")

#         except json.JSONDecodeError:
#             return JsonResponse({'success': False, 'error': 'Invalid JSON data'}, status=400)
#         except Exception as e:
#             print(f"Error Processing contact form: {str(e)}")
#             return JsonResponse({'success': False, 'error': 'An error occurred while processing your message'}, status=500)

#     elif request.method == 'GET':
#         # Fetch all messages from the database
#         contacts = BusinessContactMessage.objects.values('name', 'email', 'phone', 'property_type', 'message', 'created_at')
#         return JsonResponse({'success': True, 'messages': list(contacts)}, safe=False)

#     else:
#         return JsonResponse({'error': 'Only POST and GET requests are allowed'}, status=400)

@csrf_exempt  
def business_contact_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name", "")
            email = data.get("email", "")
            phone = data.get("phone", "")
            property_type = data.get("property", "")
            message = data.get("message", "")

            if not name or not email or not message:
                return JsonResponse({"success": False, "error": "All fields are required"}, status=400)

            # Save to database
            contact = BusinessContactMessage.objects.create(
                name=name, email=email, phone=phone, property_type=property_type, message=message
            )
            return JsonResponse({"success": True, "message": "Message received successfully"})

        except json.JSONDecodeError:
            return JsonResponse({"success": False, "error": "Invalid JSON data"}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "error": f"An error occurred: {str(e)}"}, status=500)

    return JsonResponse({"error": "Only POST requests are allowed"}, status=400)




# def sitemap_view(request):
#     # Generate sitemap URLS
#     urls = [
#         reverse('home'),
#         reverse('about'),
#         reverse('contact'),
#         # Add more URLs here
#     ]

#     # Create sitemap
#     sitemap_data = [
#         {
#             'location': url,
#             'lastmod': datetime.now(),
#             'changefreq': 'daily',
#             'priority': 0.8,
#         }
#         for url in urls
#     ]

#     # Return the sitemap as XML
#     return render(request, 'core/sitemap.xml', {'sitemap_data': sitemap_data}, content_type='application/xml')

# def view_message(request):
#     messages = BusinessContactMessage.objects.all()
#     return render(request, 'core/view_messages.html', {'messages': messages})

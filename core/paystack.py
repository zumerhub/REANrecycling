import requests
import uuid
from django.conf import settings


class PaystackTransaction:
    def __init__(self):
        # Ensure these are set in your Django settings
        self.secret_key = settings.PAYSTACK_SECRET_KEY
        self.public_key = settings.PAYSTACK_PUBLIC_KEY
        self.base_url = 'https://api.paystack.co'

    def initialize_transaction(self, amount, email, callback_url):
        """
        Initialize a Paystack transaction
        
        :param amount: Transaction amount in naira
        :param email: Customer's email
        :param callback_url: URL to redirect after payment
        :return: Transaction initialization response
        """
        headers = {
            'Authorization': f'Bearer {self.secret_key}',
            'Content-Type': 'application/json'
        }
        
        # Generate a unique reference
        reference = f'TX-{uuid.uuid4()}'
        
        data = {
            'amount': int(amount * 100),  # Convert to kobo (cents)
            'email': email,
            'reference': reference,
            'callback_url': callback_url
        }
        
        try:
            response = requests.post(
                f'{self.base_url}/transaction/initialize', 
                json=data, 
                headers=headers
            )
            return response.json()
        except requests.RequestException as e:
            return {
                'status': False,
                'message': str(e)
            }

    def verify_transaction(self, reference):
        """
        Verify a Paystack transaction
        
        :param reference: Transaction reference
        :return: Transaction verification result
        """
        headers = {
            'Authorization': f'Bearer {self.secret_key}'
        }
        
        try:
            response = requests.get(
                f'{self.base_url}/transaction/verify/{reference}', 
                headers=headers
            )
            return response.json()
        except requests.RequestException as e:
            return {
                'status': False,
                'message': str(e)
            }
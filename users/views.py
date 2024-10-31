from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import InternshipApplication , Contact, webhook_logs
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import InternshipApplication, webhook_logs
from .serializers import WebhookLogsSerializer

def home(request):
    return render(request, 'home.html')


def apply(request):
    return redirect("https://payments.cashfree.com/forms/stashcodes-internship")
    
    


@method_decorator(csrf_exempt, name='dispatch')
class PaymentWebhook(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        
        # Store data in webhook_logs
        try:
            log_serializer = WebhookLogsSerializer(data={'log': data})
            if log_serializer.is_valid():
                log_serializer.save()
        except Exception as e:
            pass
        
        try:
            order_status = data['data']['order']['order_status']
            customer_details = data['data']['order']['customer_details']
            
            if order_status == 'PAID':
                # Extract customer details
                customer_email = customer_details['customer_email']
                customer_name = customer_details['customer_name']
                customer_phone = customer_details['customer_phone']
                customer_fields = {field['title']: field['value'] for field in customer_details['customer_fields']}
                
                
                address = customer_fields.get('Address Line 1', '') + ', ' + customer_fields.get('City', '') + ', ' + customer_fields.get('State', '') + ', ' + customer_fields.get('Pincode', '')
                # Create a new InternshipApplication entry
                application = InternshipApplication(
                    email=customer_email,
                    name=customer_name,
                    contact=customer_phone,
                    domain=customer_fields.get('Domain of Internship ', ''),
                    address= address,
                    gender=customer_fields.get('Gender', ''),
                    college=customer_fields.get('College', ''),
                    qualification=customer_fields.get('Highest Academic Qualification', ''),
                    year=customer_fields.get('Year of Passout', ''),
                    ispaid=True
                )
                application.save()
                return Response({"status": "Success!"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Order status is not PAID."}, status=status.HTTP_400_BAD_REQUEST)
        except KeyError as e:
            return Response({"error": f"Missing key: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        except json.JSONDecodeError:
            return Response({"error": "Invalid JSON format."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": "Internal server error."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def contact_us(request):
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.message = request.POST['message']
        contact.save()
        messages.success(request, "Your message has been sent.")
        return redirect('home')
    else:
        return render(request, 'contact.html')
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

@login_required(login_url="/auth/login/google-oauth2/")
def apply(request):
    if request.method == 'POST':
        email = request.POST['email']
        domain = request.POST['domain']
        if InternshipApplication.objects.filter(Q(email=email) & Q(domain=domain)).exists():
            messages.error(request, "You have already registered with this email and domain.")
            return redirect('home')
        else:
            application = InternshipApplication()
            application.email = email
            application.name = request.POST['name']
            application.gender = request.POST['gender']
            application.domain = domain
            application.college = request.POST['college']
            application.contact = request.POST['contact']
            application.whatsapp = request.POST['whatsapp']
            application.qualification = request.POST['qualification']
            application.year = int(request.POST['year'])
            application.source = request.POST['source']
            application.save()
            messages.success(request, "Application submitted successfully.")
            return redirect("https://payments.cashfree.com/forms/stashcodes-internship")
        
        # return render(request, 'applyconfirm.html')
        
    else: 
        return render(request, 'apply.html')


@method_decorator(csrf_exempt, name='dispatch')
class PaymentWebhook(APIView):
    def post(self, request, *args, **kwargs):
        # data = request.data
        
        # # Store data in webhook_logs
        # try:
        #     log_serializer = WebhookLogsSerializer(data={'log': json.dumps(data)})
        #     if log_serializer.is_valid():
        #         log_serializer.save()
        # except:
        #     pass
       
        # else:
        #     return Response(log_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({"status": "Success!"}, status=status.HTTP_200_OK)
        
        
        # try:
        #     order_status = data['data']['order']['order_status']
        #     customer_email = data['data']['order']['customer_details']['customer_email']
            
        #     if order_status == 'PAID':
        #         application = InternshipApplication.objects.get(email=customer_email)
        #         application.ispaid = True
        #         application.save()
        #         return Response({"status": "Success!"}, status=status.HTTP_200_OK)
        #     else:
        #         return Response({"error": "Order status is not PAID."}, status=status.HTTP_400_BAD_REQUEST)
        # except KeyError as e:
        #     return Response({"error": f"Missing key: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        # except json.JSONDecodeError:
        #     return Response({"error": "Invalid JSON format."}, status=status.HTTP_400_BAD_REQUEST)
        # except InternshipApplication.DoesNotExist:
        #     return Response({"error": "Internship application not found."}, status=status.HTTP_400_BAD_REQUEST)


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
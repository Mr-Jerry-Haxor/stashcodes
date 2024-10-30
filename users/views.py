from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import InternshipApplication , Contact, webhook_logs
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

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


@csrf_exempt
def payment_webhook(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # store data in webhook_logs
            log = webhook_logs()
            log.log = json.dumps(data)
            log.save()
            
            
            order_status = data['data']['order']['order_status']
            customer_email = data['data']['order']['customer_details']['customer_email']
            
            if order_status == 'PAID':
                application = InternshipApplication.objects.get(email=customer_email)
                application.ispaid = True
                application.save()
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=400)
        except (KeyError, json.JSONDecodeError, InternshipApplication.DoesNotExist):
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=400)


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
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import InternshipApplication , Contact
from django.contrib import messages
from django.db.models import Q

def home(request):
    return render(request, 'home.html')

@login_required(login_url="/auth/login/google-oauth2/")
def apply(request):
    if request.method == 'POST':
        email = request.POST['email']
        domain = request.POST['domain']
        if InternshipApplication.objects.filter(Q(email=email) & Q(domain=domain)).exists():
            messages.error(request, "You have already registered with this email and domain.")
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
        
        # return render(request, 'applyconfirm.html')
        return redirect("https://payments.cashfree.com/forms/stashcodes-internship")
    else: 
        return render(request, 'apply.html')

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
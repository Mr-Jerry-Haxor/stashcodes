from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import InternshipApplication


def home(request):
    return render(request, 'home.html')

@login_required(login_url="/auth/login/google-oauth2/")
def apply(request):
    if request.method == 'POST':
        application = InternshipApplication()
        application.email = request.POST['email']
        application.name = request.POST['name']
        application.gender = request.POST['gender']
        application.domain = request.POST['domain']
        application.college = request.POST['college']
        application.contact = request.POST['contact']
        application.whatsapp = request.POST['whatsapp']
        application.qualification = request.POST['qualification']
        application.year = int(request.POST['year'])
        application.source = request.POST['source']
        application.save()
        return redirect('home')
    else: 
        return render(request, 'apply.html')
    
    
from .models import Contact

def contact_us(request):
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.message = request.POST['message']
        contact.save()
        return redirect('home')
    else:
        return render(request, 'contact.html')
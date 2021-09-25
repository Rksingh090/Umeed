from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
# Create your views here.
def homepage(request):
    if request.method == 'POST':
        name = request.POST.get('enqname')
        mobile_no = request.POST.get('enqmobileno')
        property_type = request.POST.get('enqproperty')
        budget = request.POST.get('enqbudget')
        
        form = EnquiryForm(name=name,mobile_no=mobile_no,property_type=property_type,budget=budget)
        form.save()
    return render(request,'homeapp/index.html')

def aboutpage(request):
    return render(request,'homeapp/about-us.html')

def patnapage(request):
    return render(request,'homeapp/patna-property.html')

def biharpage(request):
    return render(request,'homeapp/bihar-property.html')

def servicepage(request):
    return render(request,'homeapp/service.html')

def technologypage(request):
    return render(request,'homeapp/technology.html')

def careerpage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        filename = request.FILES['filename']
        message = request.POST.get('message')
        print(filename)
        form = CareerForm(name=name,email=email,mobile_no=mobile_no,filename=filename,message=message)
        form.save()
    return render(request,'homeapp/career.html')

def contactpage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        form = ContactForm(name=name,email=email,mobile_no=mobile_no,subject=subject,message=message)
        form.save()
    return render(request,'homeapp/contact-us.html')

def modal_submitpage(request):
    if request.method == 'POST':
        name = request.POST.get('modalname')
        email = request.POST.get('modalemail')
        mobile_no = request.POST.get('modalmobileno')
        message = request.POST.get('modalmessage')
        modalform = ModalForm(name=name,email=email,mobile_no=mobile_no,message=message)
        modalform.save()
    return redirect(homepage)

def bihar_property_contactpage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        message = request.POST.get('message')
        form = BiharPropertyContactForm(name=name,email=email,mobile_no=mobile_no,message=message)
        form.save()
    return redirect(biharpage)

def patna_property_contactpage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        message = request.POST.get('message')
        form = PatnaPropertyContactForm(name=name,email=email,mobile_no=mobile_no,message=message)
        form.save()
    return redirect(patnapage)


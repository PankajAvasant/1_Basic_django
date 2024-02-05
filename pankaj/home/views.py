from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact  #this is for generating the object of the model
from django.contrib import messages


# Code for video: 6
def index(request):
    context = {
        'variable1':"this is sent",
        'variable2':"this is sent2"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is services page")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, "contact information got saved...")

    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")

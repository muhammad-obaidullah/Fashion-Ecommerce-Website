from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from math import ceil
from .models import Product, Contact

def home(request):
    return render(request, 'home.html')


def eidcollection(request):
    allprods = []
    prod = Product.objects.filter(collection_name = "Eid Collection")
    # print(prod);
    n = len(prod)
    nSlides = n // 4 + ceil((n/4) - (n//4))
    # print(nSlides);
    allprods.append([prod, range(1, nSlides), nSlides])
    print(allprods)
    params = {'allprods' : allprods}
    return render(request, 'eidcollection.html', params)

def summercollection(request):
    allprods = []
    prod = Product.objects.filter(collection_name = "Summer Collection")
    n = len(prod)
    print(n)
    nSlides = n // 4 + ceil((n/4) - (n//4))
    allprods.append([prod, range(1, nSlides), nSlides])
    params = {'allprods' : allprods}
    return render(request, 'summercollection.html', params)

def productview(request, myid):
    product = Product.objects.filter(id = myid)
    return render(request, 'prodview.html', {'product': product[0]})

def about(request):
    return render(request, 'about.html')

def contact(request):
    thank = False
    name = request.POST.get('name', " ") 
    email = request.POST.get('email', " ") 
    phone = request.POST.get('phone', " ") 
    desc = request.POST.get('desc', " ")
    if request.method == "POST" and len(phone) and len(email) and len(name) > 3:
        contact = Contact(name = name, email = email, phone = phone, desc = desc)
        contact.save()
        thank = True
        subject='SaintsByDawood: Thankyou For Contacting Us!'
        message='Right Place and Right Choice, Choose the Best!'
        sendfrom='settings.EMAIL_HOST_USER'
        toaddress=['obaidullahdsk@gmail.com', email]
        send_mail(subject,message,sendfrom,toaddress)
        return render(request, 'contact.html', {'thank' : thank})
    else:
        return render(request, 'contact.html')
# Create your views here.

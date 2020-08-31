from django.urls import path
from .models import Product 

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('eidcollection/', views.eidcollection, name='eidCollection'),
    path('summercollection/', views.summercollection, name='summercollection'),
    path('eidcollection/products/<int:myid>', views.productview, name='productview'),
    path('summercollection/products/<int:myid>', views.productview, name='productview'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
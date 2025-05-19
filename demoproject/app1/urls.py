from django.urls import path
from . views import AboutApi,CareerApi,ContactApi


urlpatterns=[
    path('about/',AboutApi,name='about_url'),
    path('contact/',ContactApi,name='contact_url'),
    path('carrer/',CareerApi,name='career_url')
]
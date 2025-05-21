"""
URL configuration for demoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app1.views import AboutApi,CareerApi,ContactApi,HomePage,AboutPage,ContactPage,MynfoView,Mycontact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/',ContactApi),
    path('about/',AboutApi),
    path('career/',CareerApi),
    path('homepg/',HomePage,name='home_url'),
    path('aboutpg/',AboutPage,name='about_url'),
    path('contctpg/',ContactPage,name='contact_url'),
    path('info/',MynfoView),
    path('mycon/<str:nm>/',Mycontact),
    path('',include('app1.urls'))
    

    
]

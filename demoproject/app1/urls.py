from django.urls import path

from .views import Mycontact

urlpatterns = [
    path('mycont/<str:nm>/', Mycontact, name='mycontact_url'),  
]

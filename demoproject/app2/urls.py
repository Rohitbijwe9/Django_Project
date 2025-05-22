from django.urls import path
from . views import HomeView,projectview,contactview


urlpatterns=[
    path('homep/',HomeView,name='homepg_url'),
    path('project/',projectview,name='project_url'),
    path('contct/',contactview,name='contactpg_url')

]
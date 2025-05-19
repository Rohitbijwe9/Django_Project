from django.shortcuts import render
from django.http import HttpResponse



def AboutApi(request):
    return HttpResponse('This is about page')



def ContactApi(request):
    return HttpResponse('This is contact page')


def CareerApi(request):
    return HttpResponse('This is Carrer page')




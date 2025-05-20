from django.shortcuts import render
from django.http import HttpResponse







def AboutApi(request):
    return HttpResponse('This is about page')



def ContactApi(request):
    return HttpResponse('This is contact page')


def CareerApi(request):
    return HttpResponse('This is Carrer page')




# for html template render

def HomePage(request):
    template_name='app1/home.html'
    return render(request,template_name)


def AboutPage(request):
    template_name='app1/about.html'
    return render(request,template_name)


def ContactPage(request):
    template_name='app1/contact.html'
    return render(request,template_name)




#info form

def MynfoView(request):
    print(request.method)

    id=None
    nm=None
    if request.method == 'POST':
        id=request.POST.get('id')
        nm=request.POST.get('nm')
    print(id)
    print(nm)
    template_name='app1/info.html'
    return render(request,template_name)



def Mycontact(request, nm):
    return HttpResponse(f'Hello  {nm}')
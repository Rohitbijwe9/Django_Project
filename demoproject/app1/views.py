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



def contextview(request):
    template_name='app1/context.html'
    l=[2,3,5,7,8,1,0,9]
    
    context={'data':l}
    return render(request,template_name,context)


class Student:
    def __init__(self,roll,nm,marks):
        self.roll = roll
        self.name = nm
        self.marks = marks

S1=Student(9,'rohit',75)
S2=Student(7,'priti',70)
S3=Student(6,'akshay',77)


def studentView(request):
    template_name='app1/student.html'
    s_list=[S1,S2,S3]
    context={'data':s_list}
    return render(request,template_name,context)

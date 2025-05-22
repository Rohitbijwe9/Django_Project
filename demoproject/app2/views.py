from django.shortcuts import render


def HomeView(request):
    template_name='app2/home.html'
    context={}
    return render(request,template_name,context)




def projectview(request):
    template_name='app2/projects.html'
    context={}
    return render(request,template_name,context)


def contactview(request):
    template_name='app2/contact.html'
    context={}
    return render(request,template_name,context)


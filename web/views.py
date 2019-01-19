from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'web/home.html', {'activate' : 'home'})


def about(request):
    return render(request, 'web/about.html',  { 'activate' : 'about'})


def contact(request):
    return render(request, 'web/contact.html',  {'activate' : 'contact'})


def faqs(request):
    return render(request, 'web/faqs.html',  {'activate' : 'faqs'})


def services(request):
    return render(request, 'web/services.html',  {'activate' : 'services'})


def blog(request):
    return render(request, 'web/blog.html',  {'activate' : 'blog'})

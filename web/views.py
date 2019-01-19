from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'web/home.html')


def about(request):
    return render(request, 'web/about.html')


def contact(request):
    return render(request, 'web/contact.html')


def faqs(request):
    return render(request, 'web/faqs.html')


def services(request):
    return render(request, 'web/services.html')


def blog(request):
    return render(request, 'web/blog.html')

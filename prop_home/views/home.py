from django.shortcuts import render

def get_home(request):
    return render(request, "home/get-home.html")

def about_us(request):
    return render(request, "home/about-us.html")

def contact_us(request):
    return render(request, "home/contact-us.html")

def get_gallery(request):
    return render(request, "home/get-gallery.html")

def facility(request):
    return render(request, "home/facilities.html")
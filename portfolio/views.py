from django.shortcuts import render

def index(request):
    return render(request, 'portfolio/index.html')

def about(request):
    return render(request, 'portfolio/page1.html')

def merak(request):
    return render(request, 'portfolio/coming_soon.html')

def learning_journey(request):
    return render(request, 'portfolio/about_me.html')

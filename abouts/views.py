from django.shortcuts import render

def home(request):
    return render(request, 'abouts/home.html')

def about(request):
    return render(request, 'abouts/about.html')

def contacts(request):
    return render(request, 'abouts/contacts.html')

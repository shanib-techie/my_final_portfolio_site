from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    return render(request, 'main/projects.html')

def skills(request):
    return render(request, 'main/skills.html')

def contact(request):
    return render(request, 'main/contact.html')

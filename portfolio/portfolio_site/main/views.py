from django.shortcuts import render ,redirect
from .models import Contact
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def projects(request):
    return render(request, 'main/projects.html')

def skills(request):
    return render(request, 'main/skills.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        return redirect("main:contact")

    return render(request, 'main/contact.html')
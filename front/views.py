from django.shortcuts import render
from home.models import Post , Home
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your views here.

def index(request):
    home = Home.objects.filter(slug="home").first()
    aboutus = Home.objects.filter(slug="about").first()
    recenteducation = Home.objects.filter(slug="recenteducation")
    honors = Home.objects.filter(slug="honors_and_awards").first()

    skills = Home.objects.filter(slug="skills")
    experience = Home.objects.filter(slug="experience")
    project = Home.objects.filter(slug="project")
    certifications = Home.objects.filter(slug="certifications")

    return render(request ,'front/index.html' , {'home': home , 'aboutus': aboutus , 'recenteducation': recenteducation , 'honors': honors , 'skills': skills , 'experience': experience , 'project': project , 'certifications': certifications})


def aboutus(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        errors = {}

        if len(name) < 2:
            errors['name'] = ['name field is required.']
        try:
            validate_email(email)
        except ValidationError:
            errors['email'] = ['Please enter a valid email address.']
        if len(subject) < 3:
            errors['subject'] = ['Subject must be at least 3 characters long.']
        if len(message) < 10:
            errors['message'] = ['Message must be at least 10 characters long.']

        if errors:
            return JsonResponse({'errors': errors}, status=400)
        else:
            email_body = f"""
            You have a new contact form submission:

            Name: {name}
            Email: {email}
            Subject: {subject}
            Message:
            {message}
            """

            send_mail(
                    subject=f"New contact form submission: {subject}",
                    message=email_body,  # Include all details here
                    from_email=email,  # The email entered in the form
                    recipient_list=[settings.EMAIL_HOST_USER],  # Send to your email
                    fail_silently=False,
                )
            return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
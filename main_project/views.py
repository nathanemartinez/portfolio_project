from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail

# *** HOME PAGE ***
def index(request):
    return render(request, 'basic_pages/home.html', {})


def projects(request):
    return render(request, 'basic_pages/projects.html', {})


def about(request):
    return render(request, 'basic_pages/about.html', {})


# TESTERS
def tester1(request):
    return render(request, 'testers/tester1.html', {})


def tester2(request):
    subject = 'You are invited'
    message = "Hello there"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['nathanemtz@gmail.com']
    auth_user = settings.EMAIL_HOST_USER
    auth_password = settings.EMAIL_HOST_PASSWORD
    # datatuple = (subject, message, from_email, recipient_list)
    # send_mass_mail(
    #     datatuple=(datatuple,), fail_silently=False, auth_user=auth_user, auth_password=auth_password,
    # )
    send_mail(subject, message, from_email, recipient_list, fail_silently=False, auth_user=auth_user, auth_password=auth_password)

    context = {
        'subject': subject
    }
    return render(request, 'testers/tester2.html', context)


# *** ERROR PAGES ***
def error_400(request, exception=None):
    context = {}
    return render(request, 'error_pages/400.html', context)


def error_403(request, exception=None):
    context = {}
    return render(request, 'error_pages/403.html', context)


def error_404(request, exception=None):
    context = {}
    return render(request, 'error_pages/404.html', context)


def error_500(request):
    context = {}
    return render(request, 'error_pages/500.html', context)


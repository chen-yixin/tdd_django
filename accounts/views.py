from django.contrib import auth, messages
from django.core.mail import send_mail
from django.urls import reverse
from django.shortcuts import redirect
import os
from accounts.models import Token


def send_login_email(request):
    email = request.POST.get('email')
    token = Token.objects.create(email=email)
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    message_body = f'Use this link to log in:\n\n{url}'
    send_mail(
        'Your login link for Superlists',
        message_body,
        os.environ.get('EMAIL_USER', 'noreply@superlists'),
        [email]
    )
    messages.success(
        request,
        "Check your email, we've sent you a link you can use to log in."
    )
    return redirect('/')


def login(request):
    user = auth.authenticate(request.GET.get('token'))
    if user:
        auth.login(request, user)
    return redirect('/')


def logout(request):
    auth.logout(request)
    return redirect('/')

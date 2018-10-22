from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseNotFound
from ui import settings
from ui.forms import *
from core.utils import *
from user_mgr import processing as um


def login_view(request):
    if request.user.is_authenticated:
        return redirect(normalize_url(settings.DASHBOARD_URL))

    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = um.get_user_by_email(form.cleaned_data['email'])
            if user is not None:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return JsonResponse({'status': 'success', 'redirect_url': normalize_url(settings.DASHBOARD_URL)},
                                    status=200)
            else:
                return JsonResponse({'status': 'failed', 'message': {'username': 'such user does not exist'}},
                                    status=400)
        else:
            return JsonResponse({'status': 'failed', 'message': form.errors}, status=400)


# TODO rework with email registration
def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = um.create_user(username=form.cleaned_data['username'],
                                  email=form.cleaned_data['email'],
                                  password=form.cleaned_data['password'])

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return JsonResponse({'status': 'success', 'redirect_url': normalize_url(settings.DASHBOARD_URL)},
                                status=200)
        else:
            return JsonResponse({'status': 'failed', 'message': form.errors}, status=400)


def logout_view(request):
    logout(request)
    return redirect(normalize_url(settings.LOGIN_URL))

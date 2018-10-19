from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseNotFound
from . import settings
from .forms import *


def normalize_url(url):
    if not url.startswith('/'):
        return '/' + url
    return url


def index(request):
    if request.user.is_authenticated:
        return redirect(normalize_url(settings.DASHBOARD_URL))
    else:
        return redirect(normalize_url(settings.LOGIN_URL))


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', context={'header_message': 'hello world!'})


def auth_view(request):
    if request.user.is_authenticated:
        return redirect(normalize_url(settings.DASHBOARD_URL))

    if request.method == 'GET':
        return render(request, 'login.html')

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=form.cleaned_data['email'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return JsonResponse({'status': 'success', 'redirect_url': normalize_url(settings.BOOKING_URL)},
                                    status=200)
            else:
                return JsonResponse({'status': 'failed', 'message': {'username': 'such user does not exist'}},
                                    status=400)
        else:
            return JsonResponse({'status': 'failed', 'message': form.errors}, status=400)


def register_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        # User.objects.create_user(username=form.cleaned_data['username'],
        #                          password=form.cleaned_data['password'])
        user = authenticate(request,
                            username=form.cleaned_data['username'],
                            password=form.cleaned_data['password'])
        login(request, user)
        return JsonResponse({'status': 'success', 'redirect_url': normalize_url(settings.BOOKING_URL)},
                            status=200)
    else:
        return JsonResponse({'status': 'failed', 'message': form.errors}, status=400)


def logout_view(request):
    logout(request)
    return redirect(normalize_url(settings.LOGIN_URL))


@login_required
def create_project(request):
    pass

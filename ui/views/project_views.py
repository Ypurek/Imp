from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseNotFound
from ui import settings
from ui.forms import *
from core.utils import *
from user_mgr import processing as um


def index(request):
    if request.user.is_authenticated:
        return redirect(normalize_url(settings.DASHBOARD_URL))
    else:
        return redirect(normalize_url(settings.LOGIN_URL))


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', context={'header_message': 'hello world!'})


@login_required
def create_project(request):
    pass

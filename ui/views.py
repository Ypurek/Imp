from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    return render(request, 'dashboard.html', context={'header_message': 'hello world!'})


@login_required
def create_project(request):
    pass

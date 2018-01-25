from core.models import Project
from core import project_manager as pm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotAllowed
import json


@login_required
def create_project(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(('POST',))

    body = json.loads(request.body)
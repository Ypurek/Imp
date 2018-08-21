from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
import json


@login_required
def create_project(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(('POST',))

    body = json.loads(request.body)
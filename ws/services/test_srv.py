from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, JsonResponse
from core.forms import CreateTestForm
from core.managers import project_manager as pm
from user_mgr import processing as um
import json


@login_required
def get_test(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(('GET',))

    owner = request.user.owned_projects
    part = request.user.visible_projects
    response = []
    if owner is not None:
        for proj in owner:
            response.append({'projectId': proj.id,
                             'projectName': proj.name,
                             'projectDescription': proj.description,
                             'userRole': 'owner'})
    if part is not None:
        for proj in part:
            response.append({'projectId': proj.id,
                             'projectName': proj.name,
                             'projectDescription': proj.description,
                             'userRole': 'participant'})
    return JsonResponse(response, status=200)


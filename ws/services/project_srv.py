from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, JsonResponse
from core.forms import CreateProjectForm
from core.managers import project_manager as pm
from user_mgr import processing as um
import json


@login_required
def get_projects(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(('GET',))

    owner = request.user.owned_projects
    part = request.user.visible_projects
    response = {'owner': [],
                'participant': []}
    if owner is not None:
        for proj in owner:
            response['owner'].append({'projectId': proj.id,
                                      'projectName': proj.name,
                                      'projectDescription': proj.description})
    if part is not None:
        for proj in part:
            response['part'].append({'projectId': proj.id,
                                     'projectName': proj.name,
                                     'projectDescription': proj.description})
    return JsonResponse(response, status=200)


# TODO user add by email or whatever
@login_required
def create_project(request):
    if request.method != 'POST':
        return HttpResponseNotAllowed(('POST',))

    f = CreateProjectForm(request.POST)
    if f.is_valid():
        project = pm.create_project(user=request.user,
                                    name=f.cleaned_data['projectName'],
                                    description=f.cleaned_data['projectDescription'])
        if f.cleaned_data['users'] is not None:
            for username in f.cleaned_data['users']:
                pm.add_user(project, um.get_user_by_name(username))
        return JsonResponse({'projectId': project.id,
                             'projectName': project.name,
                             'projectDescription': project.description},
                            status=201)
    else:
        return JsonResponse({'status': 'failed', 'message': f.errors}, status=400)
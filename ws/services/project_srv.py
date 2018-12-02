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

    name = request.GET.get('name')
    description = request.GET.get('description')

    projects = pm.search_project(request.user, name, description)

    return JsonResponse([{'projectId': project.id,
                          'projectName': project.name,
                          'projectDescription': project.description} for project in projects],
                        status=200)


@login_required
def get_project(request, id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(('GET',))
    try:
        proj_id = int(id)
    except ValueError:
        return JsonResponse({'error': 'wrong id format'}, status=400)
    except TypeError:
        # TODO check
        return JsonResponse({'error': 'wrong id format. check if possible'}, status=400)

    project = pm.get_project(proj_id)
    if project is None:
        return JsonResponse({'error': 'project does not exist or no rights to get it'}, status=400)

    if project.check_permission(request.user):
        return JsonResponse({'projectId': project.id,
                             'projectName': project.name,
                             'projectDescription': project.description},
                            status=200)
    else:
        return JsonResponse({'error': 'project does not exist or no rights to get it'}, status=400)


@login_required
def add_users(request, proj_id):
    if request.method != 'POST':
        return HttpResponseNotAllowed(('POST',))
    # TODO


@login_required
def remove_users(request, proj_id):
    if request.method != 'POST':
        return HttpResponseNotAllowed(('POST',))
    # TODO
